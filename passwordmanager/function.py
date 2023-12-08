# This is for functionality
from tkinter import END, messagebox
import json

class functions:
            
    # def a function to generate password 
    def generate_password():        
        
        from design import designs
        from gui import GUI
        from random import randint, choice, shuffle
        from pyperclip import copy
                
        GUI.entry3.delete(0, END)
        website_or_account = GUI.entry1.get()
        
        if len(website_or_account)==0:
            messagebox.showinfo("NO", message="It's required to enter something in the website_or_account field")
        else:
            password_letter = [choice(designs.letters) for _ in range(randint(6, 9))]
            password_number = [choice(designs.numbers) for _ in range(randint(2, 6))]
            password_symbol = [choice(designs.symbols) for _ in range(randint(2, 6))]
            
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
        from gui import GUI        
            
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
            is_ok = messagebox.askokcancel(title="Details will be saved as",
                                           message=f"Email/Username: {email_or_username}\nPassword: {password}\nIs it ok to save?")
                
            if is_ok:
                try:
                    with open("password_data.json", "r") as password_data_file:
                        # read/ load up the old password data file
                        password_data = json.load(password_data_file)
                        
                except FileNotFoundError:
                    with open("password_data.json", "w") as password_data_file:
                        json.dump(new_password_data, password_data_file, indent=4)
                        
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
    
    
    def search_password():
        from gui import GUI
        
        website_or_account = GUI.entry1.get()
        try:
            with open("password_data.json") as password_data_file:
                password_data = json.load(password_data_file)        
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No data found")
        else:        
            if website_or_account in password_data:
                username_or_email = password_data[website_or_account]["email/username"]
                password = password_data[website_or_account]["password"]
                messagebox.showinfo(title=website_or_account, message=f"Email: {username_or_email}\nPassword: {password}")
            else:
                messagebox.showinfo(title="Error", message="No data found")
       
                
                
        
        
            
        
    
                   














# ----------------------- # TEST ANOTHER STRUCTURE DESIGN # ----------------------- #

# def add_password():
#     import main
#     website_or_account = main.entry1.get()
#     email_or_username = main.entry2.get()
#     password = main.entry3.get()
            
#     if len(website_or_account)==0 or len(password)==0:
#         messagebox.showinfo(title="NO", message="It's required to enter something in the field/s")
#     else:
#         is_ok = messagebox.askokcancel(title=main.label1, message=f"There are the details entered:\nEmail/Username: {email_or_username}\nPassword: {password}\nIs it ok to save?")
#         if is_ok:
#             with open("password_data.txt", "a") as password_data:
#                 password_data.write(f"{website_or_account} | {email_or_username} | {password}\n")
#                 main.entry1.delete(0, END)
#                 main.entry3.delete(0, END)