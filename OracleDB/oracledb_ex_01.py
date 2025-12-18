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