from tkinter import *
from tkinter import messagebox
import random
from typing import TextIO

import pyperclip
import json

def generate_password():
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']
    nr_letter=random.randint(8,10)
    nr_number=random.randint(4,6)
    nr_symbols=random.randint(1,3)

    password_list=[]
    for char in range(nr_letter):
        password_list.append(random.choice(LOCASE_CHARACTERS))

    for num in range(nr_number):
        password_list.append(random.choice(DIGITS))

    for sym in range(nr_symbols):
        password_list.append(random.choice(SYMBOLS))

    random.shuffle(password_list)

    password_num=""
    for char in password_list:
        password_num+=char

    password.insert(0,password_num)
    pyperclip.copy(password_num)
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    passwords=password.get()
    new_data={
        website:{
            "email":email,
            "password":passwords
        }
    }

    if len(website)==0 or len(passwords)==0:
        messagebox.showinfo(title="Oops",message="you cannot leave website or password blank")
    else:
        is_ok=messagebox.askokcancel(title=f"{website}",message="Do you want to save this ?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    data=json.load(data_file)
                    data.update(new_data)

            except:
                with open("data.json","w") as data_fil:
                    json.dump(new_data,data_fil,indent=4)
            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(new_data,data_file,indent=4)

            finally:
                website_entry.delete(0,END)
                password.delete(0, END)

def search_website():
    website=website_entry.get()

    with open("data.json","r") as data_file:
        data=json.load(data_file)
        if website in data:
            email=data[website]["email"]
            password=data[website]["password"]
            messagebox.showinfo(title=website,message=f" {website} email : {email}\n{website} password :{password}")
        else:
            messagebox.showerror(title=website,message=f"{website} is not saved yet!")

# ---------------------------- SAVE PASSWORD ------------------------------- #
window=Tk()
window.title("password manager")
window.config(padx=40,pady=40)
canvas= Canvas(height=200,width=200)


logo_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website")
website_label.grid(column=0,row=1)
email_label=Label(text="email ")
email_label.grid(column=0,row=2)
password_entry=Label(text=" password ")
password_entry.grid(row=3,column=0)

website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"gungunbali.hky@gmail.com")
password=Entry(width=21)
password.grid(row=3,column=1)


search_button=Button(text="Search",width=14,command=search_website)
search_button.grid(column=2,row=1)
generate_pass=Button(text="Generate Password",width=14,command=generate_password)
generate_pass.grid(row=3,column=2)
add_button=Button(text="Add",width=30,command=save)
add_button.grid(row=4,column=1,columnspan=2)


# ---------------------------- UI SETUP ------------------------------- #
window.mainloop()