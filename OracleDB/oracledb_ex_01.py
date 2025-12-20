''''   Software and Database Software. To do this we need to learn the following the Steps.
****************************************************************************************************
Step-1: import Appropriate Data Base Module and Other Modules if required.
Step-2: Every Python Program Must Obtain the Connection from Database Software
Step-3: Every Python Program Must  Create an object of Cursor
Step-4: Every Python Program Must Design the Query ,Place the Query in Cursor object and send for Executing in
               Database.
Step-5: Every Python Program Must Process the Result of the Query which is coming from Data Base through Cursor
             object
Step-6: Every Python Program is Recommned to Close the Connection from Database Software (Optional )
****************************************************************************************************'''

# import oracledb
# print(oracledb.__version__)

#=======================================================================================================================

import oracledb as orc # Step-1
try:
    conobj=orc.connect("system/tiger@localhost/orcl") #step-1
    print("Python Program Got Connection from Oracle Database")
    print("Type of conobj=",type(conobj))
except orc.DatabaseError as db:
    print("\tProblem in Oracle db:", db)

#=======================================================================================================================

# OracleConnectionTestEx3.py
import oracledb as orc  # Step-1

try:
    conobj = orc.connect("system/tiger@localhost/orcl")  # Step-2
    print("-----------------------------------------------")
    print("Python Program Got Connection from Oracle Database")
    print("Type of conobj=", type(conobj))
    print("-----------------------------------------------")
    curobj = conobj.cursor()  # #Step-3
    print("Python Program Created an Object of Cursor")
    print("Type of curobj=", type(curobj))
    print("-----------------------------------------------")
except orc.DatabaseError as db:
    print("\tProblem in Oracle db:", db)

#=======================================================================================================================

#Program for Creating Table --employee
#OracleTableCreateEx.py
import oracledb as orc # Step-1
def tablecreate():
    try:
        con=orc.connect("system/tiger@localhost/orcl") #Step-2
        cur=con.cursor() # Step-3
        #Step-4
        tcq="create table employee(eno number(2) primary key,name varchar2(10) not null,sal number(5,2))"
        cur.execute(tcq)
        #Step-5
        print("Table Created Sucessfully--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
#Main Program
tablecreate() # Function Call

#=======================================================================================================================

#program for Inserting Record in Employee Table
#OracleRecordInsertEx1.py
import oracledb as orc # Step-1
def recordinsert():
    try:
        con=orc.connect("system/tiger@localhost/orcl") #Step-2
        cur=con.cursor() # Step-3
        #Step-4
        iq="insert into employee values(400,'Gosling',1.7,'SUNMS')"
        cur.execute(iq)
        con.commit()
        #Step-5
        print("Record Inserted in Employee Table--verify")
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
#Main Program
recordinsert() # Function Call

#=======================================================================================================================

import oracledb #step-1

# Establish a connection (autocommit is often False by default)
connection_object = oracledb.connect('YOUR_CONNECTION_STRING') #step-2
cursor_object = connection_object.cursor() # step-3

try:
    # Execute DML statements
    cursor_object.execute("INSERT INTO employees (name, salary) VALUES (?, ?)", ('Sita', 50000)) #step-
    cursor_object.execute("UPDATE departments SET budget = budget - 50000 WHERE id = ?", (12345,)) #step-4

    # Commit the transaction to save the changes permanently
    connection_object.commit() #step-5
    print("Transaction committed successfully.") #step-6

except Exception as e:
    # If any error occurs, roll back the transaction to discard changes
    connection_object.rollback() #step-7
    print(f"An error occurred, rolled back: {e}")

finally:
    # Close the cursor and connection in the finally block
    if cursor_object:
        cursor_object.close() #step-8
    if connection_object:
        connection_object.close() #step-9

#=======================================================================================================================

#program for Inserting Record in Employee Table
#OracleRecordInsertEx2.py
import oracledb as orc # Step-1
def recordinsert():
    try:
        con=orc.connect("system/tiger@localhost/orcl") #Step-2
        cur=con.cursor() # Step-3
        #Accept the employee Values from Key Board
        print("-----------------------------------------")
        empno=int(input("Enter Employee Number:"))
        empname = input("Enter Employee Name:")
        empsal = float(input("Enter Employee Salary:"))
        empcompname =input("Enter Employee Comp Name:")
        print("-----------------------------------------")
        #Step-4
        iq="insert into employee values(%d,'%s',%f,'%s')" %(empno,empname,empsal,empcompname)
        cur.execute(iq)
        con.commit()
        #Step-5
        print("{} Record Inserted in Employee Table--verify".format(cur.rowcount))
    except orc.DatabaseError as db:
        print("Problem in Oracle:",db)
#Main Program
recordinsert() # Function Call

#=======================================================================================================================

# Python 3.13.1 Interpreter (Simulated)
# File: OracleRecordUpdateEx2_Fixed.py

import oracledb as orc
def recordupdate():
    con = None
    try:
        # Step-2: Establish connection once for the session
        con = orc.connect("system/tiger@localhost:1521/orcl")
        cur = con.cursor()  # Step-3

        while True:
            print("\n-------------------------------------------------")
            try:
                empno = int(input("Enter Employee Number for updating: "))
                empsal = float(input("Enter New Employee Salary: "))
                empcompname = input("Enter New Employee Comp Name: ")

                # Step-4: Using BIND VARIABLES for security and performance
                # This prevents SQL Injection and formatting errors
                uq = "update employee set sal=:1, cname=:2 where eno=:3"
                cur.execute(uq, (empsal, empcompname, empno))

                if cur.rowcount > 0:
                    con.commit()  # Commit after a successful update
                    print(f"✅ {cur.rowcount} Record Updated successfully.")
                else:
                    print("❌ Employee Number Does not Exist.")

            except ValueError:
                print("⚠️ Invalid Input! Please enter numeric values for ID and Salary.")
            print("-------------------------------------------------")
            ch = input("Do you want to update another record (yes/no): ").strip().lower()
            if ch == "no":
                print("Thx for Using this Program")
                break

    except orc.DatabaseError as db:
        print("Problem in Oracle:", db)
    finally:
        # Step-5: Ensure connection is closed even if an error occurs
        if con:
            con.close()
            print("Oracle Connection Closed.")
# Main Program
if __name__ == "__main__":
    recordupdate()

#=======================================================================================================================

import oracledb as orc

def recordupdate_advanced():
    con = None
    try:
        # Step-2: Establish connection
        con = orc.connect("system/tiger@localhost:1521/orcl")
        cur = con.cursor()

        updated_count = 0
        print("--- Bulk Update Mode Started ---")

        while True:
            print("\n" + "-" * 40)
            try:
                empno = int(input("Enter Employee Number to update: "))
                empsal = float(input("Enter New Salary: "))
                empcompname = input("Enter New Company Name: ")

                # Step-4: Prepare the update in the buffer
                uq = "update employee set sal=:1, cname=:2 where eno=:3"
                cur.execute(uq, (empsal, empcompname, empno))

                if cur.rowcount > 0:
                    updated_count += cur.rowcount
                    print(f"✔️ Update for ID {empno} prepared in memory.")
                else:
                    print(f"❌ Employee {empno} not found. No change prepared.")

            except ValueError:
                print("⚠️ Invalid input! Skipping this entry.")

            print("-" * 40)
            ch = input("Add another update to this transaction? (yes/no): ").strip().lower()
            if ch == "no":
                break

        # --- STRATEGY A: Final Decision Point ---
        if updated_count > 0:
            print(f"\nSummary: {updated_count} updates are waiting to be saved.")
            confirm = input("Confirm all changes? (yes to COMMIT / no to ROLLBACK): ").strip().lower()

            if confirm == "yes":
                con.commit()
                print("✅ DATABASE UPDATED: All changes saved permanently.")
            else:
                con.rollback()
                print("↩️ ROLLBACK EXECUTED: All changes discarded.")
        else:
            print("No updates were performed.")

    # --- STRATEGY B: Graceful DB Error Handling ---
    except orc.DatabaseError as db:
        print("\n🔥 A Database Error Occurred!")
        if con:
            con.rollback()
            print("↩️ Emergency Rollback performed to protect data integrity.")
        print("Error Details:", db)

    finally:
        if con:
            con.close()
            print("\nOracle Connection Closed.")

if __name__ == "__main__":
    recordupdate_advanced()

'''This script demonstrates a professional **PDBC transaction management** system using two specific strategies 
to ensure data integrity.

 🚩 The Problem
By default, every `execute()` call can be committed immediately, which is risky. If you have 10 updates and the 5th
 fails, or you realize you made a typo, you can't undo the previous 4.

 ✅ The Solution (Main Points)
1.  **Buffered Execution:** The code calls `cur.execute()` inside the loop but **delays** `con.commit()`.
 This keeps changes in a "pending" state in memory.
 
2.  **Strategy A (Bulk Decision):** It uses a **Final Decision Point** outside the loop. 
 This allows the user to review all changes as a single batch and either save all (**COMMIT**) 
 or undo all (**ROLLBACK**) at once.
 
3.  **Strategy B (Emergency Rollback):** The `except` block catches `orc.DatabaseError`. If the database crashes or 
 a constraint is violated, it triggers an **automatic rollback** to prevent partial or corrupted data from being saved.
 
4.  **Resource Safety:** The `finally` block ensures `con.close()` is always called, preventing connection leaks.
'''

#=======================================================================================================================
