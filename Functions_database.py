import sqlite3
from tkinter import *
from tkinter import messagebox as mb

#Creating root window and connecting database with our program
conn = sqlite3.connect("Rte.db")
cur = conn.cursor()

def Create_table():
    """Using this particular funtion we are creating all necessary tables in our database.
    """
    cur.execute("CREATE TABLE if not exists total_birth (Father_Name TEXT, Date_of_birth DATE, Ration_Status TEXT, Child_Name TEXT)");
    conn.commit()
    
    cur.execute("CREATE TABLE if not exists school_admission (Stu_Name Text, Father_Name Text, Date_of_birth Date)");
    conn.commit()

    cur.execute("CREATE TABLE if not exists UnAdmissionStudent( Father_Name TEXT, Date_of_birth DATE, Ration_Status TEXT,Studnet_name TEXT)")
    conn.commit()

def fetch_data():
    """Using this particular funtion we are fetching all necessary data from our database.
    """
    cur.execute("select * from UnAdmissionStudent order by Studnet_name")
    return cur.fetchall()
