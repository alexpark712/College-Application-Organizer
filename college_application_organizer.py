# College Application Organizer 
# By: Alex Park

# This program receives input information from the user regarding certain details about their college applications and sorts all the information into an 
# table that is organized and able to be copy and pasted for reproduction on other mediums such as documents. 

from __future__ import print_function
import numpy as np 
from tabulate import tabulate

def prerequisites():
    college_name = input("College Name: ")
    print("-----------------------------------")
    application_status = input("ED / EA / RD: ")
    print("-----------------------------------")
    application_due_date = input("Application Due Date: ")
    print("-----------------------------------")
    application_type = input("Common Application / Coalition Application / School Application: ")
    print("-----------------------------------")
    supplemental_essays = input("Number of Supplemental Essays: ")
    print("-----------------------------------")
    application_fee = input("Application Fee: ")
    print("-----------------------------------")
    testing = input("SAT / ACT / None (Type all that apply): ")
    print("-----------------------------------")
    financial_aid = input("FAFSA / CSS / Other (Type all that apply): ")
    return [college_name, application_status, application_due_date, application_type, supplemental_essays, application_fee, testing, financial_aid]


def list_generator():
    college_list = []
    while True:
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        question = input("Type ADD to add school to list or QUIT to end program and generate the list: ")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
        if question == "ADD":
            college_list.append(prerequisites())
            continue
        if question == "QUIT":
            return college_list
            break 

def table_maker():
    data = list_generator() 
    m = np.array(data)
    headers = ["College Name", "Application Status", "Application Due Date", "Application Type", "Supplemental Essays", 
    "Application Fee", "Standardized Test Acceptance", "Financial Aid Application"]
    table = tabulate(m, headers, tablefmt = "simple")
    print("")
    print(table)
    print("")
    print("Feel free to copy and paste this table and keep track of your college application information!")
    print("")

table_maker()





