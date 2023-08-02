from tkinter import *

# PASSWORD GENERATOR

# SAVE PASSWORD

def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    with open('data.txt', 'a') as data_file:
        data_file.write(f'{website} | {email} | {password}\n')
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# UI SETUP

window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text='Website')
website_label.grid(row=1, column=0)
email_label = Label(text='Email/UserName')
email_label.grid(row=2, column=0)
password_label = Label(text='Password')
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, 'USER@MAIL.COM')
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# buttons
generate_button = Button(text='Generate Password')
generate_button.grid(row=3, column=2)
add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
