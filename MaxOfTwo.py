from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
def max_of_two(): #This is a function
    num1 = int(AEntry.get())
    num2 = int(BEntry.get())
    if num1 > num2:
        messagebox.showinfo("Max of two numbers", f"Num-1 ({num1}) is greater")
    else:
        messagebox.showinfo("Max of two numbers", f"Num-2 ({num2}) is greater")
        window = Tk()
        window.title("Max of two")
        blabel = Label(window)
        blabel.grid()
        frame = Frame(window)
        frame.place(x=600, y=100)

        A = Label(frame, text="Enter first number: ", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
        A.grid(row=0, column=0, padx=10, pady=5)

        AEntry=Entry(frame, width=30)
        AEntry.grid(row=0, column=1)

        B = Label(frame, text="Enter second number:", font=('Arial', 15, 'bold'), bg='white', fg='firebrick')
        B.grid(row=1, column=0, padx=10, pady=5)

        BEntry = Entry(frame, width=30)
        BEntry.grid(row=1, column=1)

        submit_button = Button(frame, text="Submit", command=max_of_two)
        submit_button.grid(row=2, column=1)

        window.mainloop()
