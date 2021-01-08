from tkinter import *
import os
from datetime import *
import time
from helpers.dates import *
import mysql
import mysql.connector

# Database
db = mysql.connector.connect(
    host="localhost",
    user='root',
    passwd='Thepassword59..',
    database="plannerapp"
)


mycursor = db.cursor()


root = Tk()
root.geometry("500x250")
root.title("Task App")


class showTask():

    def __init__(self, master):
        self.label = Label(master, text="Test")
        self.label.grid(row=1, column=1)


# todo Create frame for punchclock class
class PunchClock():

    def __init__(self, master):
        self.clock = Label(master, text="TIME", font=("Helvetica", 48), fg="green", bg="black")
        self.clock.grid(row=0, column=1, padx=50)
        self.clock.after(500, self.clockEngine)

    def clockEngine(self):
        self.hour = time.strftime("%H")
        self.minute = time.strftime("%M")
        self.second = time.strftime("%S")
        self.clock.config(text=self.hour + ":" + self.minute + ":" + self.second)
        self.clock.after(1000, self.clockEngine)

    # todo timer method for punchclock
    def timer(self):
        pass


#todo create columns in database for task completeion date
#todo fix date dropdown menus, make dates match month date
class MainScreen():

    def __init__(self, master):

        #Frames
        self.taskFrame = LabelFrame(master)
        self.taskFrame.grid(row=0, column=1, pady=5)
        self.sideBar = LabelFrame(master, padx=10, pady=16)
        self.sideBar.grid(row=0, column=0, padx=10, pady=5)

        #Labels
        self.taskLabel = Label(self.taskFrame, text="Task")
        self.taskLabel.grid(row=0, column=2)
        self.deadlineLabel = Label(self.taskFrame, text="Deadline")
        self.deadlineLabel.grid(row=2, column=2)

        #Entry
        self.taskEntry = Entry(self.taskFrame)
        self.taskEntry.grid(row=1, column=2)

        #buttons
        self.homeButton = Button(self.sideBar, text="Home", command=self.homeFunc)
        self.homeButton.grid(row=0, column=0)
        self.punchclockButton = Button(self.sideBar, text="PunchClock", command=self.punchclockClicked)
        self.punchclockButton.grid(row=3, column=0)
        self.settingsButton = Button(self.sideBar, text="Settings", padx=12, command=self.settingsButton)
        self.settingsButton.grid(row=4, column=0)
        self.confirmButton = Button(self.taskFrame, text="Add Task", command=self.addTask)
        self.confirmButton.grid(row=5, column=2, pady=10)
        self.shareButton = Button(self.sideBar, text="Share Task", padx=5)
        self.shareButton.grid(row=2, column=0)
        self.viewTask = Button(self.sideBar, text="View Task", padx=7, command=self.viewTask)
        self.viewTask.grid(row=1, column=0)

        #combobox
        self.monthVar = StringVar()
        self.monthVar.set(month[0])
        self.monthDrop = OptionMenu(self.taskFrame, self.monthVar, *month)
        self.monthDrop.grid(row=3, column=0)

        self.monthDay = list(range(32))
        self.monthDayVar = StringVar()
        self.monthDayVar.set(self.monthDay[0])
        self.monthDayDrop = OptionMenu(self.taskFrame, self.monthDayVar, *self.monthDay)
        self.monthDayDrop.grid(row=3, column=1)

        self.dayVar = StringVar()
        self.dayVar.set(day[0])
        self.dayDrop = OptionMenu(self.taskFrame, self.dayVar, *day)
        self.dayDrop.grid(row=3, column=2)

        self.hour = list(range(13))
        self.hourVar = StringVar()
        self.hourVar.set(self.hour[0])
        self.hourDrop = OptionMenu(self.taskFrame, self.hourVar, *self.hour)
        self.hourDrop.grid(row=3, column=3)

        self.minute = list(range(60))
        self.minuteVar = StringVar()
        self.minuteVar.set(self.minute[0])
        self.minuteDrop = OptionMenu(self.taskFrame, self.minuteVar, *self.minute)
        self.minuteDrop.grid(row=3, column=4)


    def addTask(self):
        #gets task info
        self.task = self.taskEntry.get()
        self.dateStart = datetime.now()
        self.deadlineMonth = self.monthVar.get()
        self.deadlineMonthDay = self.monthDayVar.get()
        self.deadlineDay = self.dayVar.get()
        self.deadlineHour = self.hourVar.get()
        self.deadlineMinute = self.minuteVar.get()

        #prints task info
        print(self.task)
        print(self.dateStart)
        print(self.deadlineMonth)
        print(self.deadlineMonthDay)
        print(self.deadlineDay)
        print(self.deadlineHour)
        print(self.deadlineMinute)

        #add task to database
        mycursor.execute("INSERT INTO task(TaskName, created) VALUES(%s,%s)", (self.task, self.dateStart))
        db.commit()

        #clear task entry
        self.taskEntry.delete(0, END)

    def punchclockClicked(self):
        self.taskFrame.destroy()
        PunchClock(root)

    def settingsButton(self):
        print("Clicked")

    def homeFunc(self):
        #fixme: if home button clicked more than once you cant change screens
        MainScreen(root)

    def viewTask(self):
        self.taskFrame.destroy()
        showTask(root)


if __name__ == "__main__":
    MainScreen(root)
    root.mainloop()

