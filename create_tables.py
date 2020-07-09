import sqlite3
def Create_table():
    conn = sqlite3.connect("Rte.db")
    cur = conn.cursor()
"""The below statement will create a table of birth of children in a particular district,
in a particular year, for example year is 2012.
 """
    cur.execute("CREATE TABLE total_birth (Father_Name TEXT, Date_of_birth DATE, Ration_Status TEXT, Child_Name TEXT)");
    conn.commit()
"""The below statement will create a table of total no. of admissions in class 1st in year 2018 and 2019. """
    cur.execute("CREATE TABLE school_admission (Stu_Name Text, Father_Name Text, Date_of_birth Date)");
    conn.commit()
    conn.close()

Create_table()
print("Table created")

