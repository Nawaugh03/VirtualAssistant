from DatabaseManager import DBmanager as DB

A = DB("localhost", "root", "1234")
A.ExportFromCSV("PracticeDataset.csv")
A.UseDatabase("Memory")