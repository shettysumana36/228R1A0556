from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def max_of_three():
    num1 = int(num1Entry.get())
    num2 = int(num2Entry.get())
    num3 = int(num3Entry.get())
    if num1 >= num2 and num1 >= num3:
        messagebox.showinfo("Max of three numbers", f"Num-1 ({num1}) is greater")
    elif num2 >= num1 and num2 >= num3:
        messagebox.showinfo("Max of three numbers", f"Num-2 ({num2}) is greater")
    else:
        messagebox.showinfo("Max of three numbers", f"Num-3 ({num3}) is greater")

        window = Tk()
        window.title("Max of three")
        blabel = Label(window)
        blabel.grid()
        frame = Frame(window)
        frame.place(x=600, y=100)

        num1 = Label(frame, text="Enter first number: ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
        num1.grid(row=0, column=0, padx=10, pady=5)

        num1Entry = Entry(frame, width=30)
        num1Entry.grid(row=0, column=1)

        num2 = Label(frame, text="Enter second number: ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
        num2.grid(row=1, column=0, padx=10, pady=5)

        num2Entry = Entry(frame, width=30)
        num2Entry.grid(row=1, column=1)

        num3 = Label(frame, text="Enter third number: ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
        num3.grid(row=2, column=0, padx=10, pady=5)

        num3Entry = Entry(frame, width=30)
        num3Entry.grid(row=2, column=1)

        submit_button = Button(frame, text="Submit", command=max_of_three)
        submit_button.grid(row=3, coloumn=1)

        window.mainloop()