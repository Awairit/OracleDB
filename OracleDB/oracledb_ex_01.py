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