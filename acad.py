# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 16:01:19 2021

@author: USER
"""

from tkinter import *
from tkinter import W,E,END
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
from tkcalendar import Calendar, DateEntry
import tkinter as tk
import os
import random
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode
from datetime import datetime


def Clear():
    global surname_entry, firstname_entry, middlename_entry, stkvar, dtkvar,research_interest_entry,da,number_entry,mail_entry
    surname_entry.delete(0, END)
    firstname_entry.delete(0, END)
    middlename_entry.delete(0, END)
    dtkvar.set('choose department')
    stkvar.set('choose status')
    research_interest_entry.delete(0,END)
    da.delete(0, END)
    number_entry.delete(0, END)
    mail_entry.delete(0, END)
    

def Exit():
    global win
    mb = tk.messagebox.askquestion("Question", "Are you sure you want to quit")
    if (mb == 'yes'):
        win.destroy()
    else:
        tk.messagebox.showinfo('Return','You will now return to the application' )
    win.mainloop()

def insert_data():
    global l5, my_str,surname_entry, firstname_entry, middlename_entry, stkvar, dtkvar,research_interest_entry,da,number_entry,mail_entry
    flag_validation = True#set the flag
    surname =surname_entry.get()
    firstname = firstname_entry.get()
    middlename= middlename_entry.get()
    department = dtkvar.get()
    status = stkvar.get()
    research_interest = research_interest_entry.get()
    date = da.get()
    
    
    number = number_entry.get()
    mail = mail_entry.get()
    
    #ensuring no empty entry field
    s = len(surname)
    f = len(firstname)
    n = len(number)
    m = len(mail)
    
   
    if (s<2) or (f<2) or (n<2) or (m<2) or (department == "choose department") or (status == "choose status"):
        flag_validation = False
    try :
        val = int(number)
    except:
        flag_validation=False
    
    if (flag_validation):
        my_str.set("Adding data...")
        try:
            
            #add your mysql details
            connection = mysql.connector.connect(host='localhost',
                                     database='oau_tech_faculty',
                                     user='root',
                                     password='root')
            
            query = """INSERT INTO oau_tech_academic_staff(Surname, First_Name, Middle_Name, Department, Present_Status, Research_Interest,Date_of_Last_Promotion, Phone_No, Email_Address) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
            my_data = (surname, firstname, middlename,department,status,research_interest,date,number,mail)
        
            cursor = connection.cursor()
            cursor.execute(query, my_data)# inserting the data
            connection.commit()
            cursor.close()
            
            #resetting the entries
            surname_entry.delete(0, END)
            firstname_entry.delete(0, END)
            middlename_entry.delete(0, END)
            dtkvar.set('choose department')
            stkvar.set('choose status')
            research_interest_entry.delete(0,END)
            da.delete(0, END)
            number_entry.delete(0, END)
            mail_entry.delete(0, END)
            l5.grid()
            l5.config(fg='green')
            l5.config(bg='white')
            my_str.set("Added successfully")
            l5.after(3000,lambda:l5.grid_remove())
                    
        except Error as e:
            error = str(e.__dict__['orig'])
            l5.grid()
            #return error
            l5.config(fg='red')
            l5.config(bg='yellow')
            #print(error)
            my_str.set(error)
            
            
    else:
        l5.config(fg='blue')#foreground colour
        l5.config(bg='brown')#background colour
        my_str.set("check inputs")

def acad_window():
    global win, l5, my_str,surname_entry, firstname_entry, middlename_entry, stkvar, dtkvar,research_interest_entry,da,number_entry,mail_entry

#The window creation
    win = tk.Tk()
    win.resizable(0, 0)
    #window.iconbitmap(r'icoin.ico')
    win.title('OAU Faculty of Technology Promotional Form')
    win.geometry('500x300')

    #The Label creation
    surname_label = ttk.Label(win, text='Surname :')
    firstname_label = ttk.Label(win, text='Firstname :')
    middlename_label = ttk.Label(win, text='Middlename :')
    department_label = ttk.Label(win, text='Department :')
    present_status_label = ttk.Label(win, text='Present Status :')
    date_of_last_promotion_label = ttk.Label(win,text='Date of Last Promotion :')
    research_interest_label = ttk.Label(win, text='Research Interest :')
    number_label = ttk.Label(win,text='Phone Number :')
    mail_label = ttk.Label(win,text='Email Address :')

    val_x = 0
    val_y = 5

    surname_label.grid(row=0, column=1, sticky=W, pady=val_y, padx=val_x)
    firstname_label.grid(row=1, column=1, sticky=W, pady=val_y, padx=val_x)
    middlename_label.grid(row=2, column=1, sticky=W, pady=val_y, padx=val_x)
    department_label.grid(row=3, column=1, sticky=W, pady=val_y, padx=val_x)
    present_status_label.grid(row=4, column=1, sticky=W, pady=val_y, padx=val_x)
    date_of_last_promotion_label.grid(row=5, column=1, sticky=W, pady=val_y, padx=val_x)
    research_interest_label.grid(row=6, column=1, sticky=W, pady=val_y, padx=val_x)
    number_label.grid(row=7, column=1, sticky=W, pady=val_y, padx=val_x)
    mail_label.grid(row=8, column=1, sticky=W, pady=val_y, padx=val_x)

    #Entry fields creation
    surname_entry = ttk.Entry(win)
    firstname_entry = ttk.Entry(win)
    middlename_entry = ttk.Entry(win)
    
    departments = ['choose department','Computer Science & Engineering', 'Mechanical Engineering', 'Electrical Engineering', 'Material Science & Engineering', 'Civil Engineering', 'AISPI','Chemical Engineering','Food Science and Technology','Agricultural and Enviromental Engineering']
    dtkvar = tk.StringVar(win)
    dtkvar.set([0])#default option

    stkvar = tk.StringVar(win)
    status = ['choose status','Professor','Reader','Senior Lecturer', 'Lecturer 1', 'Lecturer 2', 'Assistant Lecturer', 'Graduate Assistant', 'Principal Research Fellow', 'Senior Research Fellow', 'Research Fellow I', 'Research Fellow II']
    stkvar.set([0])

    research_interest_entry = ttk.Entry(win)
    number_entry = ttk.Entry(win)
    mail_entry = ttk.Entry(win)
    
    val_x = 3
    val_y = 3

    surname_entry.grid(row=0, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
    firstname_entry.grid(row=1, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
    middlename_entry.grid(row=2, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)

    dop= ttk.OptionMenu(win, dtkvar, *departments)
    dop.grid(row = 3, column= 2, padx=(2,15), ipadx=val_x, ipady=val_y)

    sop = ttk.OptionMenu(win,stkvar, *status )
    sop.grid(row = 4, column= 2, padx=(2,15), ipadx=val_x, ipady=val_y)

    da = DateEntry(win, width=20, bg="darkblue",fg="white",year=2021)

    da.grid(row = 5, column = 2)

    research_interest_entry.grid(row=6, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
    number_entry.grid(row=7, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)
    mail_entry.grid(row=8, column=2, padx=(2, 15), ipadx=val_x, ipady=val_y)

    #Creating exception for empty entry field
    my_str = tk.StringVar(win)
    l5 = tk.Label( win,textvariable=my_str, width=15 )  
    l5.grid(row=3,column=3)
    my_str.set("Output")


    #Creating the buttons

    submit = ttk.Button(win,text='Submit', command=insert_data, width=17, )
    submit.grid(row=9, column=1, sticky=E + W, padx=2, ipadx=3, ipady=3)

    clear = ttk.Button(win,text='Clear', command=Clear, )
    clear.grid(row=9, column=2, sticky=E + W, pady=5, padx=(2, 15), ipadx=3, ipady=3)

    exi = ttk.Button(win,text='Exit', command=Exit )
    exi.grid(row=9, column=3, columnspan=2, sticky=W + E,padx=(2, 15), pady=5, ipadx=3, ipady=3)

    win.mainloop()
    return win

if __name__=='__main__':
    acad_window()