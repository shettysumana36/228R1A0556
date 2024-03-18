from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image

def is_leap_year():
    year=int(LeapYearEntry.get())
    if(year%4==0 and year%100!=0) or (year%400==0)
        messagebox.showinfo("Output","It is a leap year")
    else:
        messagebox.showinfo("Output","It is not an leap year")

        window=Tk()
        window.title("Leap Year")
        blabel=Label(window)
        blabel.grid()
        frame=Frame(window)
        frame.place(x=600,y=100)

        Leap_yearlabel=Label(frame,text="Enter an year",font=('Arial',15,'bold'),bg='white',fg='firebrick')
        Leap_yearlabel.grid(row=0,c)