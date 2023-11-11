from tkinter import (
    Tk, Label, BOTTOM, IntVar,
    Spinbox, StringVar, Entry, Button
)
import pyperclip
import random
import string

root = Tk()
root.geometry("350x250")
root.resizable(0, 0)
root.title("Password Generator")

Label(root, text="Password Generator", font="arial 20 bold").pack()
Label(root, text="DataFlair", font="arial 15 bold").pack(side=BOTTOM)

pass_label = Label(root, text="Password Length", font="arial 10 bold")
pass_label.pack()

pass_len = IntVar()
length = Spinbox(root, from_=8, to=32, textvariable=pass_len, width=15)
length.pack()

pass_str = StringVar()


def Generator():
    password = ''

    for x in range(0, 4):
        password += random.choice(string.ascii_uppercase)
        + random.choice(string.ascii_lowercase) + random.choice(string.digits)
        + random.choice(string.punctuation)

    for y in range(pass_len.get()):
        password += random.choice(string.ascii_uppercase +
                                  string.ascii_lowercase + string.digits +
                                  string.punctuation)

    pass_str.set(password)


Button(root, text="Generate password", command=Generator).pack(pady=5)
Entry(root, textvariable=pass_str).pack()


def copy_password():
    pyperclip.copy(pass_str.get())


Button(root, text="Copy to clipboard", command=copy_password).pack(pady=5)

root.mainloop()
