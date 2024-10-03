from tkinter import *

FONT = ("Arial", 18)

def button_clicked():
    print("I got clicked")
    milesVar = input.get()
    kmResult = int(milesVar) * 1.6
    my_label.config(text=kmResult)


window = Tk()
window.title("My First GUI Program")
window.config(padx=30, pady=30)

#Label
isEqualTo = Label(text="is equal to", font=FONT)
isEqualTo.grid(column=0, row=1)

miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

km = Label(text="km", font=FONT)
km.grid(column=2, row=1)

my_label = Label(text="0", font=FONT)
my_label.grid(column=1, row=1)

#Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)

window.mainloop()