from gui import GUI
GUI.masterwindow.mainloop()



























# ----------------------- # TEST ANOTHER STRUCTURE DESIGN # ----------------------- #
# import tkinter as tk
# from design import designs
# from function import DataRecorder
# import function

# masterwindow = tk.Tk()
# masterwindow.title("Password manager")
# masterwindow.config(width=200, height=200, padx=20, pady=20, background=designs.bgcolor)


# # title
# title_label = tk.Label(text="Password Manager", 
#                        fg=designs.title_label_color,
#                        bg=designs.bgcolor,
#                        font=designs.title_label_font)
# title_label.grid(column=1, row=0, columnspan=3)


# # canvas
# mastercanvas = tk.Canvas(width=80, height=80,
#                          highlightthickness=0,
#                          background=designs.bgcolor)
# center_image = tk.PhotoImage(file=designs.center_image_file)
# mastercanvas.create_image(40,40, image=center_image)
# mastercanvas.grid(column=1, row=1, pady=20, columnspan=3)

# # labels
# label1 = tk.Label(text="Website", 
#                   fg=designs.label_color,
#                   bg=designs.bgcolor,
#                   font=designs.label_font)
# label1.grid(column=0, row=2, padx=5)

# label2 = tk.Label(text="Email/Username", 
#                   fg=designs.label_color,
#                   bg=designs.bgcolor,
#                   font=designs.label_font)
# label2.grid(column=0, row=3, padx=5)

# label3 = tk.Label(text="Password", 
#                   fg=designs.label_color,
#                   bg=designs.bgcolor,
#                   font=designs.label_font)
# label3.grid(column=0, row=4, padx=5)

# # buttons
# button1 = tk.Button(text="Generate password",
#                    fg=designs.button_color,
#                    bg=designs.bgcolor,
#                    font=designs.button_font, 
#                    width=18)
# button1.grid(column=2, row=4, pady=2)

# button2 = tk.Button(text="Add", width=44,
#                    fg=designs.button_color,
#                    bg=designs.bgcolor,
#                    font=designs.button_font,
#                    command=function.add_password)
# button2.grid(column=1, row=5, columnspan=2, pady=2)

# # entries
# entry1 = tk.Entry(width=44, font=designs.button_font)
# entry1.grid(column=1, row=2, columnspan=2, pady=2)
# entry1.focus()

# entry2 = tk.Entry(width=44, font=designs.button_font)
# entry2.grid(column=1, row=3, columnspan=2, pady=2)
# entry2.insert(0, "example@something.something")

# entry3 = tk.Entry(width=25, font=designs.button_font)
# entry3.grid(column=1, row=4, pady=2)

# masterwindow.mainloop()