import mysql.connector
from os import path
import csv
class DBmanager():
    def __init__(self, hostname="", username="", passwrd="", databasename=""):
        self.databasename = databasename
        self.hostname = hostname
        self.username = username
        self.password = passwrd

        if (self.databasename==""):
            self.DBconnection = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
            self.tables=[]
        else:
            if(self.isDbExist(databasename)):
                self.CreateNewDatabase(self.databasename)
            else:
                pass
            self.DBconnection = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password,
                                                    database=self.databasename)
            self.tables = self.GenerateTables()

    def GetTables(self):
        a = self.DBconnection.cursor()
        code = """SHOW TABLES;"""
        a.execute(code)
        List = []
        for items in a.fetchall():
            List.append(items[0])
        a.close()
        return List
    
    
    def isDbExist(self,dbname):
        temp = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
        a = temp.cursor()
        code = """SHOW databases;"""
        a.execute(code)
        for x in a.fetchall():
            if (dbname == x[0]):
                a.close()
                temp.close()
                return True
        return False
    def isTableExist(self, Tablename):
        cursor=self.DBconnection.cursor()
        code=f"show tables;"
        cursor.execute(code)
        #print(Tablename)
        for a in cursor.fetchall():
            if (a is None):
                cursor.close()
                return False
            else:
                for i in a:
                    if(Tablename.lower() == i):
                        cursor.close()
                        return True
                return False    
        
        
    def removeTablefromList(self, Tablename):
        for index in range(len(self.tables)):
            if(Tablename.lower() in self.tables[index].Name.lower()):
                self.tables.remove(self.tables[index])
   

    def CreateNewDatabase(self,dbname):
        if (self.isDbExist(dbname)):
            pass
        else:
            temp = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
            a = temp.cursor()
            code = f"""CREATE DATABASE {dbname}"""
            a.execute(code)
            temp.commit()
            a.close()
            temp.close()
    def DropCurrentDatabase(self):
        self.DBconnection.close()
        temp = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password)
        a =temp.cursor()
        code = f"""DROP Database {self.databasename}"""
        a.execute(code)
        temp.commit()
        self.DBconnection=temp
        a.close()
        temp.close()
    def UseDatabase(self, dbname):
        a=self.DBconnection.cursor()
        code=f"""use {dbname.lower()}"""
        try:
            a.execute(code)
            self.DBconnection.commit()
            a.close()
        except:
            self.CreateNewDatabase(dbname.lower())
            a.execute(code)
            self.DBconnection.commit()
            a.close()
            
        self.tables=self.GenerateTables()
    def GetTableContent(self, table):
        a = self.DBconnection.cursor()
        code = f"""SELECT * FROM {table};"""
        a.execute(code)
        List = []
        for items in a.fetchall():
            List.append(items)
        a.close()
        return List
    def GetTableDescription(self, tablename):
        a=self.DBconnection.cursor()
        code = f"""DESCRIBE {tablename};"""
        a.execute(code)
        List=[]
        for items in a.fetchall():
            List.append(items)
        a.close()
        return List
    def GenerateTables(self):
        ListofTables=[]
        for i in range(len(self.GetTables())):
            Tablename=self.GetTables()[i]
            ListofTables.append(Table(Tablename,self.GetTableContent(Tablename), self.GetTableDescription(Tablename)))
        return ListofTables
    def DisplayTables(self):
        if (self.tables==[]):
            print("No table listed")
        for i in self.tables:
            print(i.Name)
    def ImportToCSV(self, Table):#This function allow to import one table into a csv tile
        with open (f"{Table.Name}.csv",'a',newline="") as csvfile:
            columnnames=[]
            for i in range(len(Table.Description)):
                columnnames.append(Table.Description[i][0])
            writer=csv.writer(csvfile)
            writer.writerow(columnnames)
            for content in (Table.Content):
                writer.writerow(content)
    
    def ExportFromCSV(self, csvname):
        if (self.isTableExist(csvname) is False):
            pass
        else:
            self.removeTablefromList(csvname)
        Newtable=Table(csvname)
        Tablecolumnnames=None
        Tablecontent=[]
        with open(f"{csvname}.csv",'r')as csvfile:
            reader=csv.reader(csvfile)
            rownumber=0
            for row in reader:
                if (rownumber==0):
                    Tablecolumnnames=row
                elif(rownumber>0):
                    Tablecontent.append(row)
                    #print(Tablecontent)
                rownumber=rownumber+1
        Newtable.GetColumnnames(Tablecolumnnames)
        Newtable.Getcontent(Tablecontent)
        Newtable.GenerateDatatypes()
        self.tables.append(Newtable)
        #Newtable.showinfo()
        #print(self.tables)

            #UPDate table
    def DeleteTableFromSQL(self,Table):
        #temp = mysql.connector.connect(host=self.hostname, user=self.username, password=self.password,database=self.databasename)
        cursor=self.DBconnection.cursor()
        code=f"""DROP TABLES {Table.Name};"""
        cursor.execute(code)
        self.DBconnection.commit()
        cursor.close()
    def ImportTablestoSQL(self):
        for tableindex in range(len(self.tables)):#number of tables
            if(self.isTableExist(self.tables[tableindex].Name)):
                self.DeleteTableFromSQL(self.tables[tableindex])
            a = self.DBconnection.cursor()
            tablecode=f"CREATE TABLE {self.tables[tableindex].Name} (\n"
            rownum = 0
            totalrows=len(self.tables[tableindex].columnnames)
            #print(totalrows)
            #print(self.tables[tableindex].columntypes[0])
            #create a table
            for index in range(totalrows):#number of columns
                datatype=self.tables[tableindex].columntypes[index]
                columnname=self.tables[tableindex].columnnames[index]
                
                tablecode+=f"{columnname} {datatype}"
                if (rownum<totalrows-1):
                    tablecode+=",\n"    
                else:
                    tablecode+="\n"
                rownum+=1
            tablecode+=");"
            rownum=1
            #print(tablecode)# execute statement
            a.execute(tablecode)
            self.DBconnection.commit()
            a.close()

            """Place the content into the table in the sql system"""
            
            AllColumnnames=""
            for columnindex in range(totalrows):
                AllColumnnames+=str(self.tables[tableindex].columnnames[columnindex])
                if(columnindex<(totalrows-1)):
                    AllColumnnames+=","
            Insertcode=f"INSERT INTO {self.tables[tableindex].Name} ("
            totalrows=len(self.tables[tableindex].columnnames)
            Insertcode+=str(AllColumnnames)
            Insertcode+=")\n"
                
            for items in (self.tables[tableindex].Content):
                a=self.DBconnection.cursor()
                rownum=1
                contentcode=Insertcode
                contentcode+="VALUES"
                contentcode+="("
                for itemindex in  range(totalrows):
                    if("INT" in self.tables[tableindex].columntypes[itemindex]):
                        contentcode+=str(items[itemindex])
                    else:
                        message=f"\'{items[itemindex]}\'"
                        contentcode+=message
                    if(rownum<totalrows):
                        contentcode+=","
                    else:
                        contentcode+=");"
                    rownum+=1
                #print(contentcode) #executable statement
                a.execute(contentcode)
                self.DBconnection.commit()
                a.close()
            
class Table:
    def __init__(self, Tablename, tablecontent=None, tabledescription=None):
        self.Name=Tablename
        self.Content=tablecontent
        self.columnnames = []
        self.columntypes = []
        if(tabledescription != None):
            self.Description=tabledescription
            for desc in self.Description:
                self.columnnames.append(str(desc[0]).replace('\'',''))
                self.columntypes.append(str(desc[1]).replace('b','').replace('\'',''))
        else:
            pass

    def GenerateDatatypes(self):
        #print(len(self.columnnames))
        for index in range(len(self.columnnames)):
            columnlist=[row[index] for row in self.Content]
            #print(columnlist)
            text=""
            if(not columnlist):
                text+="VARCHAR(255)"
                #print(":|")
            elif (all(element.isdigit()for element in columnlist)):
                #print("INT")
                text+="INT"
            elif(any(ele.isalnum() for ele in columnlist)):
                #print("VARCHAR(255)")
                text+="VARCHAR(255)"
            else:
                text+="VARCHAR(255)"
            self.columntypes.append(text)

    def Getcontent(self, content):
        self.Content=content
    def GetColumnnames(self, names):
        self.columnnames=names
    def showinfo(self):
        print(self.Name)
        print(self.columnnames)
        print(self.columntypes)
        print(self.Content)
"""
Use cases:
    Complete{-A=DBmanager("localhost","root","1234","test") -print(A.tables)} get table from database
    
    Complete{A=DBmanager("localhost","root","1234")
    A.UseDatabase("example_db")
    A.tables=A.GenerateTables()
    print(str(A.tables[0].columntype))}
    
    Complete csv->table
    table->sql put the table into sql, 1.) use database, 2.) 
    A.ImportToCSV(Table)//Take the content from Database, and convert the list to a table in a csv file ({COURSE, NUMBER, TITLE, CREDIT} ...)
    A.ExportFromCSV("Curriculum.csv")//Take name of file and convert the csv into the list then if the table does exist then edit the table by inserting the 
   
    Complete table->sql
    A = DBmanager("localhost", "root", "1234")
    A.ExportFromCSV("Curriculums")
    A.UseDatabase("HawkDB")
    A.ImportTablestoSQL()

    Complete sql->table
    A = DBmanager("localhost", "root", "1234","hawkdb")
    A.tables[0].showinfo()
    
    Complete table->csv
    A = DBmanager("localhost", "root", "1234","hawkdb")
    A.ImportToCSV(A.tables[0])

    Use database schima
    A = DBmanager("localhost", "root", "1234")
    A.UseDatabase("HawkDB")
"""
if __name__ in "__main__":
    #pass
    
    #"""
    A = DBmanager("localhost", "root", "1234","hawkdb")
    #A.DisplayTables() 
    A.ExportFromCSV("curriculums")
    #print(A.tables)
    #A.tables[0].showinfo()
    #A.UseDatabase("HawkDB")
    
    A.ImportTablestoSQL()
    #A.tables[0].showinfo() 
    #"""
    
    #
    #print(A.isTableExist(A.tables[0].Name))
    #print(A.isTableExist("curriculums"))
    #print(A.tables[0].columnnames)

    