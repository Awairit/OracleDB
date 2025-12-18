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

import os
import oracledb
from dotenv import load_dotenv

# This loads the variables from the .env file into Python
load_dotenv()

user = os.getenv(DB_USER)
password = os.getenv(DB_PASS)
dsn = os.getenv(DB_DSN)

print(oracledb.__version__)

#=======================================================================================================================

import oracledb as orc # Step-1
try:
    conobj=orc.connect("system/tiger@127.0.0.1/orcl")
    print("Python Program Got Connection from Oracle Database")
    print("Type of conobj=",type(conobj))
except orc.DatabaseError as db:
    print("\tProblem in Oracle db:", db)