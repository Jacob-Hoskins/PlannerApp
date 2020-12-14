from datetime import datetime, date

class TaskFoundation:

    def __init__(self, task, timeStart, dateStart, priorityLevel):
        self.task = task
        self.timeStart = timeStart
        self.dateStart = dateStart
        self.priorityLevel = priorityLevel

    def taskMeth(self):
        print("\n\nYour task is to " + task)

    def timeMeth(self):
        print("\nTask created at:\nTime: " + self.timeStart)

    def dateMeth(self):
        print("Date: " + self.dateStart)

    def priorityMeth(self):
        print("Priority Level: " + priority)

task = input("Task: ")
now = datetime.now()
today = date.today()
current_time = now.strftime("%H:%M:%S")
startDate = today.strftime("%d/%m/%Y")
priority = input("Priority level 1, 2, or 3: ")



a = TaskFoundation(task, current_time, startDate, priority)
a.taskMeth()
a.timeMeth()
a.dateMeth()
a.priorityMeth()