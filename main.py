from tkinter import *
from datetime import *
from helpers.dates import *
import mysql.connector
import time


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


class ToDo():
    def __init__(self, master):

        #Frames
        self.taskFrame = LabelFrame(master)
        self.taskFrame.grid(row=0, column=1, pady=5)
#Home Button
        self.side = LabelFrame(master)
        self.side.grid(row=0, column=0)

        #Labels
        self.taskLabel = Label(self.taskFrame, text="Task")
        self.taskLabel.grid(row=0, column=2)
        self.deadlineLabel = Label(self.taskFrame, text="Deadline")
        self.deadlineLabel.grid(row=2, column=2)

        #Entry
        self.taskEntry = Entry(self.taskFrame)
        self.taskEntry.grid(row=1, column=2)

        #buttons
        self.confirmButton = Button(self.taskFrame, text="Add Task", command=self.addTask)
        self.confirmButton.grid(row=5, column=2, pady=10)
        self.homeButton = Button(self.side, text="-\n-\n-", command=self.home, padx=20, pady=-10)
        self.homeButton.grid(row=0, column=0)

        # combobox
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
        # gets task info
        self.task = self.taskEntry.get()
        self.dateStart = datetime.now()
        self.deadlineMonth = self.monthVar.get()
        self.deadlineMonthDay = self.monthDayVar.get()
        self.deadlineDay = self.dayVar.get()
        self.deadlineHour = self.hourVar.get()
        self.deadlineMinute = self.minuteVar.get()

        # prints task info
        print(self.task)
        print(self.dateStart)
        print(self.deadlineMonth)
        print(self.deadlineMonthDay)
        print(self.deadlineDay)
        print(self.deadlineHour)
        print(self.deadlineMinute)

        # add task to database
        mycursor.execute("INSERT INTO task(TaskName, created, monthDeadline, dayDeadline,"
                         " weekDayDeadline, hourDeadline, minuteDeadline,"
                         "amPm) VALUES(%s,%s,%s,%s,%s,%s,%s)",
                         (self.task, self.dateStart, self.deadlineMonth, self.deadlineMonthDay,
                          self.deadlineDay, self.deadlineHour, self.deadlineMinute))
        db.commit()

        # clear task entry
        self.taskEntry.delete(0, END)

    def home(self):
        self.taskFrame.destroy()
        self.side.destroy()
        MainScreen(root)


class PunchClock():

    def __init__(self, master):
        # truthy statement to figure out if user has started the punchclock and how to handle input
        self.timerStart = False

        # Frames
        self.clockFrame = LabelFrame(master, pady=5)
        self.clockFrame.grid(row=0, column=1, padx=10)
        self.functionsFrame = LabelFrame(master)
        self.functionsFrame.grid(row=1, column=1)

        # Home Button
        self.side = LabelFrame(master)
        self.side.grid(row=0, column=0)

        # clock widgets
        self.homeButton = Button(self.side, text="-\n-\n-", command=self.home, padx=20, pady=-10)
        self.homeButton.grid(row=0, column=0)

        self.clock = Label(self.clockFrame, text="", font=("Helvetica", 48), fg="green", bg="black")
        self.clock.grid(row=0, column=1, padx=50)
        self.clock.after(500, self.clockEngine)

        self.startButton = Button(self.functionsFrame, text="Start time", command=self.startTime)
        self.startButton.grid(row=0, column=0)

    def clockEngine(self):
        self.hour = time.strftime("%H")
        self.minute = time.strftime("%M")
        self.second = time.strftime("%S")
        self.time = (self.hour + ":" + self.minute + ":" + self.second)
        self.clock.config(text=self.time)
        self.clock.after(500, self.clockEngine)

    # todo grab start time and upload to database
    # todo once the timer is started Truthy to see if clocks running
    def startTime(self):
        self.timerStart = True

        # check to see if timestart var is true to bring up stop and tag function
        if self.timerStart == True:
            print("You have started the time clock")
            self.time = self.hour + ":" + self.minute
            print(self.time)
            self.startButton.destroy()

            # grab start time and

            # stop button to call new function to properly stop timer and add data to DB
            self.stopButton = Button(self.functionsFrame,
                                     text="Stop Timer",
                                     command=self.stopTimer)
            self.stopButton.grid(row=0, column=0)

            # function that will bring up comment box to describe how time was spent and what got done
            self.timerDetails()

    # This function grabs data once the timer is started and uploads it to database
    def timerDetails(self):
        self.commentLabel = Label(self.functionsFrame, text="Description of time worked")
        self.commentLabel.grid(row=1, column=0)
        self.commentBox = Entry(self.functionsFrame)
        self.commentBox.grid(row=2, column=0)

    # this function will revert the clock back to its original state by changing the truthy statement to false and clearing screen
    def stopTimer(self):
        self.timerStart = False
        print(self.timerStart)
        # these destroy widgets that appear when timer is started, then return new widget that lets you restart timer
        self.stopButton.destroy()
        self.commentLabel.destroy()
        self.commentBox.destroy()
        self.newStartButton = Button(self.functionsFrame, text="Start Timer", command=self.startTime)
        self.newStartButton.grid(row=0, column=0)

    def home(self):
        self.functionsFrame.destroy()
        self.side.destroy()
        self.clockFrame.destroy()
        MainScreen(root)

#todo create columns in database for task completeion date
#todo fix date dropdown menus, make dates match month date
class MainScreen():

    def __init__(self, master):

        #Frames
        self.taskFrame = LabelFrame(master)
        self.taskFrame.grid(row=0, column=1, pady=5)
        self.sideBar = LabelFrame(master, padx=10, pady=16)
        self.sideBar.grid(row=0, column=0, padx=10, pady=5)

        #buttons
        self.toDoButton = Button(self.sideBar, text="Add Task", command=self.taskFunc)
        self.toDoButton.grid(row=1, column=0)
        self.punchclockButton = Button(self.sideBar, text="PunchClock", command=self.punchclockClicked)
        self.punchclockButton.grid(row=4, column=0)
        self.settingsButton = Button(self.sideBar, text="Settings", padx=12, command=self.settingsButton)
        self.settingsButton.grid(row=5, column=0)
        self.shareButton = Button(self.sideBar, text="Share Task", padx=5)
        self.shareButton.grid(row=3, column=0)
        self.viewTask = Button(self.sideBar, text="View Task", padx=7, command=self.viewTask)
        self.viewTask.grid(row=2, column=0)

    def taskFunc(self):
        self.taskFrame.destroy()
        self.sideBar.destroy()
        ToDo(root)

    def punchclockClicked(self):
        self.taskFrame.destroy()
        self.sideBar.destroy()
        PunchClock(root)

    def settingsButton(self):
        print("Clicked")

    def viewTask(self):
        self.taskFrame.destroy()
        self.sideBar.destroy()
        showTask(root)


if __name__ == "__main__":
    MainScreen(root)
    root.mainloop()

