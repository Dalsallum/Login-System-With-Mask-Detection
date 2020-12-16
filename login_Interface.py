import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter.ttk import *
import cv2 as cv
import numpy as np
import os
import mask_check  # the other code that will check the mask

# connect to the database of employees
conn = sqlite3.connect(r'C:\Users\komsi\Desktop\Projects\Employee_Database1.db')
cursor = conn.cursor()

root = tk.Tk()
root.title('Login')

# the next lines are used to center the interface

window_width = root.winfo_reqwidth()
window_height = root.winfo_reqheight()
pos_r = int(root.winfo_screenwidth() / 2 - window_width / 2)
pos_l = int(root.winfo_screenheight() / 2 - window_height / 2)

root.geometry("+{}+{}".format(pos_r, pos_l))

# the next lines for the label and entry of id and password

id_label = tk.Label(root, text=' ID : ').grid(row=0, column=0)
id_entry = tk.Entry(root, width=30)
id_entry.grid(row=0, column=1)

password_label = tk.Label(root, text=' Password : ').grid(row=1, column=0)
password_entry = tk.Entry(root, show="*", width=30)
password_entry.grid(row=1, column=1)


def user_click():
    '''
    when the user click Login
    '''

    user_id = id_entry.get()
    user_password = password_entry.get()

    try:  # Check the data base for the user information

        cursor.execute("select * from empl where id ='{}' and password = '{}'".format(user_id, user_password))
        emp_info = cursor.fetchone()
        messagebox.showinfo('Welcome',
                            "Welcome {} {} ! \n\nPlease WEAR your mask and be save\nThe Camera will load in a few seconds . . .".format(
                                emp_info[1].capitalize(), emp_info[2].capitalize()))

        # call the "call_cam" function from the other code which handle the detection of wearing mask
        mask_check.call_cam()

    except TypeError:
        messagebox.showerror('ERROR!', 'Wrong Informations !')


def admin_click():
    '''
     when the admin Admin login to edit the data base
    '''

    def submit_click():
        '''
        when the admin press submit
        '''

        try:  # try to execute the commands of the admin
            exec(sql_commands.get("1.0", 'end'))
            messagebox.showinfo('Done', 'Your changes have been submitted')

        except:  # show an error that the code wasn't correct
            messagebox.showerror('ERROR!', 'Could not execute, please make sure you wrote the code correctly. ')

    admin_id = id_entry.get()
    admin_password = password_entry.get()

    try:  # check the admin informations
        cursor.execute("select password from empl where id = '{}'".format(admin_id))
        database_password = cursor.fetchone()[0]
        if admin_id == 'admin' and admin_password == database_password:
            admin_window = tk.Toplevel(root)
            admin_window.title('Admin Window')
            admin_window.geometry("450x450")
            sql_commands = tk.Text(admin_window)
            sql_commands.insert('end', "cursor.execute(''' \n#Your code here\n''') \nconn.commit()")
            sql_commands.place(height=350, width=350, relx=0.5, rely=0.5, anchor='center')
            submit_button = tk.Button(admin_window, text=' Submit ', command=submit_click)
            submit_button.place(anchor='center', y=200, relx=0.5, rely=0.5, )
        else:
            messagebox.showerror('ERROR!', 'Wrong Informations !')
    except TypeError:
        messagebox.showerror('ERROR!', 'Wrong Informations !')


user_login_button = tk.Button(root, text=' Login ', command=user_click)
user_login_button.grid(row=3, column=0)

admin_button = tk.Button(root, text=' Login as Admin ', command=admin_click)
admin_button.grid(row=3, column=1)

root.mainloop()
