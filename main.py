from tkinter import *
import os
from datetime import *
from dates import month, day

root = Tk()

class MainScreen():

    def __init__(self, master):
        #Labels
        self.taskLabel = Label(master, text="Task")
        self.taskLabel.grid(row=0, column=0)
        self.deadlineLabel = Label(master, text="Deadline")
        self.deadlineLabel.grid(row=2, column=0)


        #Entry
        self.taskEntry = Entry(master)
        self.taskEntry.grid(row=1, column=0)


        #buttons
        self.punchclockButton = Button(master, text="PunchClock")
        self.punchclockButton.grid(row=0, column=1)
        self.settingsButton = Button(master, text="Settings")
        self.settingsButton.grid(row=1, column=1)
        self.confirmButton = Button(master, text="Add Task", command=self.addTask)
        self.confirmButton.grid(row=0, column=2)

        #todo add dates (1st, 3rd, 22nd etc)
        #combobox
        self.monthVar = StringVar()
        self.monthVar.set(month[0])
        self.monthDrop = OptionMenu(master, self.monthVar, *month)
        self.monthDrop.grid(row=3, column=0)
        self.dayVar = StringVar()
        self.dayVar.set(day[0])
        self.dayDrop = OptionMenu(master, self.dayVar, *day)
        self.dayDrop.grid(row=3, column=1)
        self.hour = list(range(13))
        self.hourVar = StringVar()
        self.hourVar.set(self.hour[0])
        self.hourDrop = OptionMenu(master, self.hourVar, *self.hour)
        self.hourDrop.grid(row=3, column=2)
        self.minute = list(range(60))
        self.minuteVar = StringVar()
        self.minuteVar.set(self.minute[0])
        self.minuteDrop = OptionMenu(master, self.minuteVar, *self.minute)
        self.minuteDrop.grid(row=3, column=3)

    def addTask(self):
        self.task = self.taskEntry.get()
        self.dateStart = datetime.now()
        self.deadlineMonth = self.monthVar.get()
        self.deadlineDay = self.dayVar.get()
        self.deadlineHour = self.hourVar.get()
        self.deadlineMinute = self.minuteVar.get()
        print(self.deadlineMonth)
        print(self.deadlineDay)

MainScreen(root)
root.mainloop()