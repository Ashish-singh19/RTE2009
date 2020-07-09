from Function_submit import *
from Functions_database import *
import sqlite3
from tkinter import *
from tkinter import messagebox as mb

#Creating root window and connecting database with our program
root = Tk()
conn = sqlite3.connect("Rte.db")
cur = conn.cursor()

root.title("List of Unadmission Student")
root.geometry("500x510")

""" Here we are connecting the database and GUI using Tkinter module.
"""

Create_table()
bpl_data = fetch_data()

#Defining all necessary widgets
Label(root, text = "The Complete data of students who are eligible.", relief = GROOVE, font = "Arial 13").place(x = 50, y = 0)

Label(root, text = "Search Here:").place(x = 35, y = 43)
search = Entry(root, width = 40)
search.place(x = 110, y = 43)

Label(root, text = "Student Name                 Father's Name                   Date of Birth ").place(x = 50, y = 70)
 
lb1 = Listbox(root, height = 20, width = 60)
lb1.place(x = 50, y = 90)

for i in range(len(bpl_data)):
    child_name = str(bpl_data[i][3])
    father_name = str(bpl_data[i][0])
    dob = str(bpl_data[i][1])
    lb1.insert(END, child_name + "                                     " + father_name + "                          " + dob)

def searching(e = 1):
    lb1.delete(0, END)
    possible_1 = search.get() + "%"
    possible_2 = "%" + search.get() + "%"
    possible_3 = "%" + search.get()
    cur.execute("select * from UnAdmissionStudent where (studnet_name LIKE ?) or (studnet_name LIKE ?) or (studnet_name LIKE ?) order by studnet_name", (possible_1, possible_2, possible_3))
    searched = cur.fetchall()

    for i in range(len(searched)):
        child_name = str(searched[i][3])
        father_name = str(searched[i][0])
        dob = str(searched[i][1])
        lb1.insert(END, child_name + "                                     " + father_name + "                          " + dob)
    
root.bind('<KeyPress>', searching)

#This section is for persons who could not find there name in list
Label(root, text = "Cannot find your name? Do not worry. Apply here!", relief = RAISED, font = "Arial 15").place(x = 10, y = 420)
apply_btn = Button(root, text = "Click to Apply", command = new_applications).place(x = 145, y = 455)

root.mainloop()
