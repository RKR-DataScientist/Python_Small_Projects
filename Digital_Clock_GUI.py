#  Let's import the library

from tkinter import *   
#Tkinter module belongs to a standard library of GUI in Python.

# Datetime and time modules in python help us to work with the dates and time of the current day
import datetime
import time

# Winsound module provides access to the basic sound playing machinery 
import winsound

# Let's create the while loop, it's allow to enter the function without any criteria
def alarm(alarm_timer):
    while True:
        time.sleep(1)  # it will create time thread for time interval
        current_time = datetime.datetime.now()  # it will fetch the current time

        # Let's convert the time in string format so that we could display it
        time_now = current_time.strftime("%H: %M: %S")

        # Let's convert the date in string format so that we could display it
        today_date = current_time.strftime("%d/ %m/ %y")

        print("Today Date is: ", today_date)
        print("Current Time :", time_now)

        if time_now == alarm_timer:
            # It will plays the system generated sound
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)

            break

        

def actual_time():
    alarm_timer = (f"{ hour.get() } : {min.get()}: {sec.get()}")
    alarm(alarm_timer)

#------------------ Let's Create the GUI for Digital Clocl --------------#
# Creating object
clock = Tk()
# Creating title
clock.title("Ravi Rahul Alarm Clock")
# creating window size of clock
clock.geometry("400x300")

#creating lable to set the time for alarm
time_format = Label(clock, text ="Enter time in 24 hour format! : ", fg="red",bg="black",font="Arial").place(x=80,y=200)
add_time = Label(clock, text = "Hour  Min   Sec",font=60).place(x = 170) 
# now to set the Alarm 
setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",10,"bold")).place(x=0, y=50)

# Let's create the varible for the time 
hour = StringVar()
min = StringVar()
sec = StringVar()
#Now let's create the entry space for the time
houeTime = Entry(clock, textvariable = hour, bg = "white",width = 20).place(x=150,y=50)
minTime= Entry(clock,textvariable = min, bg = "white",width = 20).place(x=200,y=50)
secTime = Entry(clock,textvariable = sec, bg = "white",width = 20).place(x=250,y=50)


#To take the time input by user:
submit = Button(clock,text = "Set Alarm",fg="red",width = 10,command = actual_time).place(x =200,y=100)
print(" Alarm has been added")
clock.mainloop()
#Execution of the window.



