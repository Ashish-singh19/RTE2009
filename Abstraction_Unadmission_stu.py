import sqlite3
conn = sqlite3.connect("Rte.db")
cur = conn.cursor()
"""The below statement will fetch all the data of children in bpl families who haven't taken admission in 
 any school yet."""
cur.execute("select * from total_birth where Ration_Status='BPL' AND total_birth.Child_Name NOT IN (select Stu_Name from school_admission )")
rows = cur.fetchall()

"""The below statements will create a table in which all the births in bpl family 
will be covered in year 2012 which haven't taken admission in any school."""
def create_table():
    cur.execute("CREATE TABLE UnAdmissionStudent( Father_Name TEXT, Date_of_birth DATE, Ration_Status TEXT,Studnet_name TEXT)")
    conn.commit()
create_table()
print("table created")
def Insert_blp_list():
    for i in rows:
        cur.execute("INSERT INTO  UnAdmissionStudent VALUES(?,?,?,?)",(i))
        conn.commit()
Insert_blp_list()
print("all done")



