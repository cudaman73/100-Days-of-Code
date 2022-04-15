from tkinter import *


def click_button():
    label3["text"] = str(int(input.get()) * 1.6)


window = Tk()
window.title("miles to km converter")
window.minsize(width=200, height=100)
window.config(padx=5, pady=5)

input = Entry(width="10")
input.focus()
input.grid(column=1, row=0)

label1 = Label(text="miles", font=("Arial", 10))
label1.grid(column=2, row=0)
label1.config(padx=5, pady=5)

label2 = Label(text="is equal to", font=("Arial", 10))
label2.grid(column=0, row=1)
label2.config(padx=5, pady=5)

label3 = Label(text="0", font=("Arial", 10))
label3.grid(column=1, row=1)
label3.config(padx=5, pady=5)

label4 = Label(text="Km", font=("Arial", 10))
label4.grid(column=2, row=1)
label4.config(padx=5, pady=5)

button = Button(text="Calculate", command=click_button)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)

window.mainloop()
