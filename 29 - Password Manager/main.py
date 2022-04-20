# This is not a real password manager - all passwords stored in plaintext, this is not safe lmao

from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    """Generates a random password with 8-10 letters, 2 - 4 numbers, 2 - 4 symbols, then
    enters it into the password form, and copies the password to the clipboard"""
    # Angela created 3 separate lists using list comprehension and added them together,
    # but I like doing it this way instead, it makes more sense to me, even if logically,
    # they are identical methods
    password_list = []
    password_list += [choice(letters) for _ in range(randint(8, 10))]
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list += [choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)

    password_text.delete(0, END)
    password_text.insert(0, password)
    # a clipboard-friendlier way would be probably to use pyperclip or some other pip module,
    # but I made the decision to do it with raw Tk commands to simplify the code. This code
    # clears the clipboard first, then adds the text.
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    """This should save the current values of the password manager in passwords.txt"""
    if website_text.get() == "" or password_text.get() == "":
        messagebox.showwarning(title="Oops", message="Double check the website/password fields")
    else:
        confirm = messagebox.askquestion(title=f"{website_text.get()}",
                                         message=f"Email/Username: {email_text.get()}\nPassword: {password_text.get()}\nIs "
                                                 f"this okay?")
        if confirm == 'yes':
            # proper formatting for file is {Website} | {Email/Username} | {Password}
            with open("passwords.txt", "a") as file:
                file.write(f"{website_text.get()} | {email_text.get()} | {password_text.get()} \n")
                website_text.delete(0, END)
                password_text.delete(0, END)
                website_text.focus()


# I wrote this ahead of the video with some minor googling, not realizing there was a messagebox module.
# I am going to leave it in the code rather than rewrite things so that hopefully, if I come back to view
# this later, I will remember there are multiple ways to do things - although some ways are harder than
# using a built in module, haha.
#
# def open_popup():
#     top = Toplevel(window)
#     top.geometry("225x100")
#     top.title(f"{website_text.get()}")
#     l = Label(top, text=f"Email/Username: {email_text.get()}\nPassword: {password_text.get()}\nIs this okay?")
#     l.grid(row=0, column=0, columnspan=2, padx=20)
#
#     b = Button(top, text="No", command=top.destroy)
#     b.grid(row=1, column=0)
#
#     b2 = Button(top, text="Yes", command=lambda: [save_password(), top.destroy()])
#     b2.grid(row=1, column=1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

logo_image = PhotoImage(file="logo.png")

logo = Canvas(height=200, width=200)
logo.create_image(100, 100, image=logo_image)
logo.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

website_text = Entry(width=52)
website_text.grid(row=1, column=1, columnspan=2)
website_text.focus()

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

email_text = Entry(width=52)
email_text.grid(row=2, column=1, columnspan=2)
email_text.insert(0, "fake@email.com")

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

password_text = Entry(width=33)
password_text.grid(row=3, column=1)

password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(row=3, column=2, pady=(0, 2))

add_button = Button(text="Add", width=44, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
