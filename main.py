from tkinter import *
import os
from datetime import *
from dates import month, day, twentyEightDays, thirtyOneDays, thirtyDays

root = Tk()

class MainScreen():

    def __init__(self, master):

        #Frames
        self.taskFrame = LabelFrame(master)
        self.taskFrame.grid(row=0, column=1)
        self.sideBar = LabelFrame(master)
        self.sideBar.grid(row=0, column=0)

        #Labels
        self.taskLabel = Label(self.taskFrame, text="Task")
        self.taskLabel.grid(row=0, column=0)
        self.deadlineLabel = Label(self.taskFrame, text="Deadline")
        self.deadlineLabel.grid(row=2, column=0)

        #Entry
        self.taskEntry = Entry(self.taskFrame)
        self.taskEntry.grid(row=1, column=0)

        #buttons
        self.punchclockButton = Button(self.sideBar, text="PunchClock", command=self.punchclockClicked)
        self.punchclockButton.grid(row=0, column=1)
        self.settingsButton = Button(self.sideBar, text="Settings")
        self.settingsButton.grid(row=1, column=1)
        self.confirmButton = Button(self.taskFrame, text="Add Task", command=self.addTask)
        self.confirmButton.grid(row=0, column=2)
        self.shareButton = Button(self.sideBar, text="Share Task")
        self.shareButton.grid(row=1, column=2)
        self.viewTask = Button(self.sideBar, text="View Task")
        self.viewTask.grid(row=0, column=3)

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
        self.task = self.taskEntry.get()
        self.dateStart = datetime.now()
        self.deadlineMonth = self.monthVar.get()
        self.deadlineMonthDay = self.monthDayVar.get()
        self.deadlineDay = self.dayVar.get()
        self.deadlineHour = self.hourVar.get()
        self.deadlineMinute = self.minuteVar.get()
        print(self.task)
        print(self.dateStart)
        print(self.deadlineMonth)
        print(self.deadlineMonthDay)
        print(self.deadlineDay)
        print(self.deadlineHour)
        print(self.deadlineMinute)

        self.taskEntry.delete(0, END)

    def punchclockClicked(self):
        print("Clicked")


#todo: create punchclock function.

MainScreen(root)
root.mainloop()