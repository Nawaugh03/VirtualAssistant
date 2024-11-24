import random
class Task:
    def __init__(self, name="", description="", priority=1, urgency=1):
        self.name = name
        self.id= random.randint(100000,999999)
        self.description = description
        self.priority = priority # 1-10
        self.urgency = urgency #1-10
        self.status = "Pending"  # Default status is Pending
        self.task_score= 0 # (Priority *0.6) + (urgency * 0.4)

    def __str__(self):
        return (f"Task: {self.name}\n"
                f"TaskID:{self.id}\n"
                f"Description: {self.description}\n"
                f"Priority: {self.priority}\n"
                f"Urgency: {self.urgency}\n"
                f"Status: {self.status}\n"
                f"Task Score: {self.task_score}")
class TaskManager:
    def __init__(self):
        self.tasks: Task = [] #Queue

    def find_task(self, id):
        if self.tasks==[]:
           return -1
        else:
           for i in len(self.tasks):
               if self.tasks[i].id==id:
                   return i
        return -1
       
       
    def SortByTaskScore(self):
        n=len(self.tasks)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if(self.tasks[j].task_score< self.tasks[min_index].task_score):
                    min_index=j
            self.tasks[i], self.tasks[min_index] = self.tasks[min_index], self.tasks[i]

    def SortByTitle(self):
        n=len(self.tasks)
        for i in range(n):
            min_index=i
            for j in range(i+1,n):
                if(self.tasks[j].task_score< self.tasks[min_index].task_score):
                    min_index=j
            self.tasks[i], self.tasks[min_index] = self.tasks[min_index], self.tasks[i]

    
    def calculateTaskScore(self, task:Task):
        taskScore=((task.priotity * 0.6 )+ (task.urgency * 0.4))
        task.task_score=taskScore

    def add_task(self,name,description,priority, urgency, status):
        TaskObj=Task()
        TaskObj.name=name
        TaskObj.description=description
        TaskObj.priority=priority
        TaskObj.urgency=urgency
        TaskObj.status=status
        self.calculateTaskScore(TaskObj)
        self.tasks.append(TaskObj)
        if len(self.tasks)>1:
            self.SortByTaskScore()

    def delete_task(self, id):
        index=self.find_task(id)
        if index != -1:
            self.tasks.pop(index)
            self.SortByTaskScore()
            
# Example Usage
if __name__ == "__main__":
   print(5*0.6 + 5*0.4)
