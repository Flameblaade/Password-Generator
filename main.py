import tkinter as tk
from tkinter.ttk import *
import string
import random


def generate_password():
    length = int(password_length.get())

    use_letters = c1_var.get()
    use_numbers = c2_var.get()
    use_special_chars = c3_var.get()

    charList = ""

    if use_letters:
        charList += string.ascii_letters

    if use_numbers:
        charList += string.digits

    if use_special_chars:
        charList += string.punctuation

    if not charList:

        return

    password = [random.choice(charList) for _ in range(length)]
    generated_password = "".join(password)

    newPass.config(state="normal")
    newPass.delete("1.0", "end")  # Fix typo in the delete method
    newPass.insert("1.0", generated_password)
    newPass.config(state="disabled")

def validate_input(char):
    return char.isdigit() or char == ""

window = tk.Tk()
window.title("Password Generator")
window.resizable(False, False)
window.geometry("300x350")

labelPassLength = Label(window, text="Enter length of your desired password")
labelPassLength.pack(pady=5)

# Entry widget where they enter the value of password length
validate_cmd = (window.register(validate_input), "%S")
password_length = tk.Entry(window, validate="key", validatecommand=validate_cmd)
password_length.pack(pady=0)
labelPassType = Label(window, text="Check what type of password you desire: ")
labelPassType.pack(pady=5)

c1_var = tk.IntVar()
c2_var = tk.IntVar()
c3_var = tk.IntVar()

c1 = tk.Checkbutton(window, text="Letters", variable=c1_var)
c2 = tk.Checkbutton(window, text="Numbers", variable=c2_var)
c3 = tk.Checkbutton(window, text="Special Characters", variable=c3_var)

c1.pack(anchor="w")
c2.pack(anchor="w")
c3.pack(anchor="w")

generatePassButton = Button(window, text="Generate Password", command=generate_password)
generatePassButton.pack()

newPass = tk.Text(window, width=30, height=1)
newPass.pack(pady=10)
newPass.config(state="normal")
newPass.insert('end', "")
newPass.config(state="disabled")

window.mainloop()
