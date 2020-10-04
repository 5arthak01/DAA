import subprocess as sp
import pymysql
import pymysql.cursors
import re
from datetime import datetime

"""
Functions to check constraints
"""
def employeeIdConstraint(id):
    try:
        constraint = True
        #add constraint for Employee_id
        if not constraint:
            print('\nIncorrect Employee ID format')
            raise ValueError
    except (AttributeError, TypeError):
        print('\nID should be string')
        raise AssertionError
    return

def phoneConstraint(phone):
    try:
        if not (len(phone)==10 or re.match('^[0-9]*$', phone)):
            print('\nPhone numbers are 10 digits')
            raise ValueError
    except (AttributeError, TypeError):
        print('\nPhone should be string')
        raise AssertionError  
    return
 
def timeConstraint(time):
    try:
        assert_time = datetime.strptime(time, '%y-%m-%d %H:%M:%S')
    except ValueError:
        print("\nTime is string YYYY-MM-DD HH:MM:SS")
        raise ValueError
    return

"""
Functions for different options
"""
def getFeedback(): # Finds specific record in Feedback 
    try:
        entry = {}
        print("Enter the Feedback details: ")
        entry['Waiter'] = input("Waiter ID: ").strip()
        entry['Chef'] = input("Chef ID: ").strip()
        entry['Dish'] = input("Dish name: ").strip()
        entry['Phone'] = input("Phone: ").strip()
        entry['Time'] = input("Time as YYYY-MM-DD HH:MM:SS ").strip()
        
        employeeIdConstraint(entry['Waiter'])  
        employeeIdConstraint(entry['Chef'])
        phoneConstraint(entry['Phone'])
        timeConstraint(entry['Time'])
        
        query = "SELECT * FROM Feedback WHERE Waiter_id=%s AND Chef_id=%s AND Dish_name=%s AND Phone=%s AND Time=%s"%(entry['Waiter'], entry['Chef'], entry['Dish'], entry['Phone'], entry['Time'])

        print(query)
        cur.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        con.commit()
        print()

    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>>>>>>>>>", e)

    return

def employeeFeedback(): # Finds all records in Feedback for given employee 
    try:
        employee = input("Enter EmployeeID: ").strip()
        
        employeeIdConstraint(employee)  

        query = "SELECT * FROM Feedback WHERE Waiter_id=%s OR Chef_id=%s"%(employee, employee)
       
        print(query)
        cur.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        con.commit()
        print()

    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>>>>>>>>>", e)

    return

def avgRating(): # Finds all records in Feedback for given employee 
    try:
        employee = input("Enter EmployeeID: ").strip()
        
        employeeIdConstraint(employee)  

        query = "SELECT * FROM Feedback WHERE Waiter_id=%s OR Chef_id=%s"%(employee, employee)
       
        print(query)
        cur.execute(query)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        con.commit()
        print()

    except Exception as e:
        con.rollback()
        print("Failed")
        print(">>>>>>>>>>>>>", e)

    return

def option2():
    """
    Function to implement option 1
    """
    print("Not implemented")


def option3():
    """
    Function to implement option 2
    """
    print("Not implemented")


def option4():
    """
    Function to implement option 3
    """
    print("Not implemented")


def hireAnEmployee():
    """
    This is a sample function implemented for the refrence.
    This example is related to the Employee Database.
    In addition to taking input, you are required to handle domain errors as well
    For example: the SSN should be only 9 characters long
    Sex should be only M or F
    If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
    """
    try:
        # Takes emplyee details as input
        row = {}
        print("Enter new employee's details: ")
        name = (input("Name (Fname Minit Lname): ")).split(' ')
        row["Fname"] = name[0]
        row["Minit"] = name[1]
        row["Lname"] = name[2]
        row["Ssn"] = input("SSN: ")
        row["Bdate"] = input("Birth Date (YYYY-MM-DD): ")
        row["Address"] = input("Address: ")
        row["Sex"] = input("Sex: ")
        row["Salary"] = float(input("Salary: "))
        row["Dno"] = int(input("Dno: "))

        query = "INSERT INTO EMPLOYEE(Fname, Minit, Lname, Ssn, Bdate, Address, Sex, Salary, Dno) VALUES('%s', '%c', '%s', '%s', '%s', '%s', '%c', %f, %d)" % (
            row["Fname"], row["Minit"], row["Lname"], row["Ssn"], row["Bdate"], row["Address"], row["Sex"], row["Salary"], row["Dno"])

        print(query)
        cur.execute(query)
        con.commit()

        print("Inserted Into Database")

    except Exception as e:
        con.rollback()
        print("Failed to insert into database")
        print(">>>>>>>>>>>>>", e)

    return


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """

    if(ch == 1):
        hireAnEmployee()
    elif(ch == 2):
        option2()
    elif(ch == 3):
        option3()
    elif(ch == 4):
        option4()
    else:
        print("Error: Invalid Option")


# Global
while(1):
    tmp = sp.call('clear', shell=True)
    
    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server 
        con = pymysql.connect(host='localhost',
                              user=username,
                              password=password,
                              db='COMPANY',
                              cursorclass=pymysql.cursors.DictCursor,
                              port=5005)
        tmp = sp.call('clear', shell=True)

        if(con.open):
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while(1):
                tmp = sp.call('clear', shell=True)
                # Here taking example of Employee Mini-world
                print("1. Option 1")  # Hire an Employee
                print("2. Option 2")  # Fire an Employee
                print("3. Option 3")  # Promote Employee
                print("4. Option 4")  # Employee Statistics
                print("5. Logout")
                ch = int(input("Enter choice> "))
                tmp = sp.call('clear', shell=True)
                if ch == 5:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call('clear', shell=True)
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
