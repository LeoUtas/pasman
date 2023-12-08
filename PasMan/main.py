# ---------------------------- GUI ELEMENT DESIGN ------------------------------- #
class elements:       
    
    # elements for designing
    center_image_file = "lock_image.png"
    
    title_label_font = ("Courier", 28, "bold")
    title_label_color = "#4b4b52"
    
    label_font = ("Courier", 12, "bold")
    label_color = "black"
    
    button_font = ("Courier", 12, "bold")
    button_color = "black"
    
    bgcolor = "white"
    
    # elements for generating password
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# ---------------------------- FUNCTIONALITY ------------------------------- #
import json
from tkinter import END, messagebox
from random import randint, choice, shuffle
from pyperclip import copy

class functions:
            
    # def a function to generate password 
    def generate_password():
                
        GUI.entry3.delete(0, END)
        website_or_account = GUI.entry1.get()
        
        if len(website_or_account)==0:
            messagebox.showinfo("NO", message="It's required to enter something in the website_or_account field")
        else:
            password_letter = [choice(elements.letters) for _ in range(randint(6, 9))]
            password_number = [choice(elements.numbers) for _ in range(randint(2, 6))]
            password_symbol = [choice(elements.symbols) for _ in range(randint(2, 6))]
            
            password = password_letter + password_number + password_symbol
            shuffle(password)
            suggested_password = "".join(password)
            hidden_password = ["*" for _ in suggested_password]
            hidden_password = "".join(hidden_password)
                    
            GUI.entry3.insert(0, suggested_password)        
            copy(suggested_password)
            return suggested_password
    
    
    # def a function to keep track of password data
    def add_password():   
        
        # make 3 entries
        website_or_account = GUI.entry1.get()
        email_or_username = GUI.entry2.get()
        password = GUI.entry3.get()
        new_password_data = {
            website_or_account: {
                "email/username": email_or_username,
                "password": password,
            }
        }
            
        if len(website_or_account)==0 or len(password)==0: # to prevent empty entries
            messagebox.showinfo(title="NO", 
                                message="It's required to enter something in the field/s")
        else:            
            is_ok = messagebox.askokcancel(title=website_or_account,
                                           message=f"Email/Username: {email_or_username}\nPassword: {password}\nIs it ok to save?")
                
            if is_ok:
                try:
                    with open("password_data.json", "r") as password_data_file:
                        # read/ load up the old password data file
                        password_data = json.load(password_data_file)
                        
                except FileNotFoundError:
                    with open("password_data.json", "w") as password_data_file:
                        json.dump(new_password_data, password_data_file, indent=4) # add new_password_data to password_data_file
                        
                else:
                    # update the old password_data with new_password_data
                    password_data.update(new_password_data)                   
                    with open("password_data.json", "w") as password_data_file:
                        # save the updated password_data_file
                        json.dump(password_data, password_data_file, indent=4)
                        # password_data.write(f"{website_or_account} | {email_or_username} | {password}\n") this is used to handle a .txt file
                finally:
                    GUI.entry1.delete(0, END)
                    GUI.entry3.delete(0, END)
    
    # def a function to search for password in the data
    def search_password():        
        
        website_or_account = GUI.entry1.get()
        try:
            with open("password_data.json") as password_data_file:
                password_data = json.load(password_data_file)        
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data found")
        else:
            if len(GUI.entry1.get())==0:
                messagebox.showinfo(message="What do you want to search?")
            else:
                # search for website/account if the information exists in the data        
                if website_or_account in password_data:
                    username_or_email = password_data[website_or_account]["email/username"]
                    password = password_data[website_or_account]["password"]
                    messagebox.showinfo(title=website_or_account, message=f"Email: {username_or_email}\nPassword: {password}")
                    copy(password)
                else:
                    messagebox.showinfo(title="Error", message="No data found")
        

# ---------------------------- GUI SETUP ------------------------------- #
import tkinter as tk

class GUI:
       
    masterwindow = tk.Tk()
    masterwindow.title("Password manager")
    masterwindow.config(width=200, height=200, padx=20, pady=20, background=elements.bgcolor)

    # title
    title_label = tk.Label(text="Password Manager", 
                        fg=elements.title_label_color,
                        bg=elements.bgcolor,
                        font=elements.title_label_font)
    title_label.grid(column=1, row=0, columnspan=3)

    # canvas
    mastercanvas = tk.Canvas(width=80, height=80,
                            highlightthickness=0,
                            background=elements.bgcolor)
    center_image = tk.PhotoImage(file=elements.center_image_file)
    mastercanvas.create_image(40,40, image=center_image)
    mastercanvas.grid(column=1, row=1, pady=20, columnspan=3)

    # labels
    label1 = tk.Label(text="Website/Account", 
                    fg=elements.label_color,
                    bg=elements.bgcolor,
                    font=elements.label_font)
    label1.grid(column=0, row=2, padx=5, pady=5)

    label2 = tk.Label(text="Email/Username", 
                    fg=elements.label_color,
                    bg=elements.bgcolor,
                    font=elements.label_font)
    label2.grid(column=0, row=3, padx=5, pady=5)

    label3 = tk.Label(text="Password", 
                    fg=elements.label_color,
                    bg=elements.bgcolor,
                    font=elements.label_font)
    label3.grid(column=0, row=4, padx=5, pady=5)

    # buttons
    button1 = tk.Button(text="Generate password",
                        width=19, borderwidth=.5,
                        fg=elements.button_color,
                        bg=elements.bgcolor,
                        font=elements.button_font,
                        command=functions.generate_password)
    button1.grid(column=2, row=4)

    button2 = tk.Button(text="Add", 
                        width=45, borderwidth=.5,
                        fg=elements.button_color,
                        bg=elements.bgcolor,
                        font=elements.button_font,
                        command=functions.add_password)
    button2.grid(column=1, row=5, columnspan=2)
    
    button3 = tk.Button(text="Search",
                        width=19, borderwidth=.5,
                        fg=elements.button_color,
                        bg=elements.bgcolor,
                        font=elements.button_font,
                        command=functions.search_password)
    button3.grid(column=2, row=2)

    # entries
    entry1 = tk.Entry(width=25, font=elements.button_font, borderwidth=2)
    entry1.grid(column=1, row=2)
    entry1.focus()

    entry2 = tk.Entry(width=45, font=elements.button_font, borderwidth=2)
    entry2.grid(column=1, row=3, columnspan=2)
    entry2.insert(0, "example@something.something")

    entry3 = tk.Entry(width=25, font=elements.button_font, borderwidth=2)
    entry3.grid(column=1, row=4)


GUI.masterwindow.mainloop()