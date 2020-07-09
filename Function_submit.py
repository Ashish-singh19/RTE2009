import sqlite3
from tkinter import *
from tkinter import messagebox as mb

#Creating root window and connecting database with our program
conn = sqlite3.connect("Rte.db")
cur = conn.cursor()

def new_applications():
    """Using this function we are taking applications from the users who could not find there name in the list.
    """
    cur.execute("create table if not exists Verifications (Child_name text, Father_name text, Date_of_birth DATE, Phone_no Number(10), Voter_ID Number(15))")
    conn.commit()

    #Making new window for application form
    root1 = Tk()
    root1.geometry("500x500")

    Label(root1, text = "Fill the form with correct details.", relief = GROOVE, font = "Arial 15").place(x = 25, y = 0)

    #Defining all the entries and respective labels
    Label(root1, text = "Child Name:").place(x = 15, y = 40)
    child_name = Entry(root1)
    child_name.place(x = 100, y = 40)

    Label(root1, text = "Father's Name:").place(x = 15, y = 80)
    father_name = Entry(root1)
    father_name.place(x = 100, y = 80)

    Label(root1, text = "Date of Birth:").place(x = 15, y = 120)
    dob_d = Entry(root1, width = 5)
    dob_d.place(x = 100, y = 120)
    dob_m = Entry(root1, width = 5)
    dob_m.place(x = 140, y = 120)
    dob_y = Entry(root1, width = 8)
    dob_y.place(x = 180, y = 120)
    Label(root1, text = "DD/MM/YYYY").place(x = 15, y = 135)

    Label(root1, text = "Phone Number:").place(x = 15, y = 170)
    Pno = Entry(root1)
    Pno.place(x = 120, y = 170)

    Label(root1, text = "Voter ID Number:").place(x = 15, y = 200)
    VID_no = Entry(root1)
    VID_no.place(x = 120, y = 200)

    def submit():
        #Inserting the data in database from entries
        #Limiting User Entry
        if len(Pno.get()) != 10:
            mb.showerror("Invalid entry", "Phone Number is Incorrect!")
        elif len(dob_y.get()) > 4 or len(dob_m.get()) > 2 or len(dob_d.get()) > 2:
            mb.showerror("Invalid entry", "Date is not valid!")
        elif int(dob_m.get()) > 12 or int(dob_d.get()) > 31:
            mb.showerror("Invalid entry", "Month or Day is incorrect!")
        elif len(VID_no.get()) == 0 or len(child_name.get()) == 0 or len(father_name.get()) == 0:
            mb.showerror("Invalid entry", "All fields are mandatory!")
        else:
            dob = dob_y.get() + "/" + dob_m.get() + "/" + dob_d.get()
            data = (child_name.get(), father_name.get(), dob, int(Pno.get()), int(VID_no.get()))
            cur.execute("insert into Verifications values (?,?,?,?,?)", data)
            conn.commit()
        
            #Clearing all entry box
            child_name.delete(0, END)
            father_name.delete(0, END)
            dob_y.delete(0, END)
            dob_m.delete(0, END)
            dob_d.delete(0, END)
            Pno.delete(0, END)
            VID_no.delete(0, END)



            mb.showinfo("Success", "Submitted successfully. You will be informed once verified")

            conn.close()
            root1.destroy()


    Button(root1, text = "Submit", command = submit).place(x = 85, y = 240)
    
    root1.mainloop()
