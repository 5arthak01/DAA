import subprocess as sp
import pymysql
import pymysql.err
import pymysql.cursors

"""
Functions for different options
"""


def get_feedback():  # Finds specific record in Feedback
    try:
        entry = {}
        print("Enter the Feedback details:- ")
        entry["Waiter"] = input("Waiter ID: ").strip()
        entry["Chef"] = input("Chef ID: ").strip()
        entry["Dish"] = input("Dish name: ").strip()
        entry["Phone"] = input("Phone: ").strip()
        entry["Time"] = input("Time as YYYY-MM-DD HH:MM:SS ").strip()

        cur.execute(
            "SELECT * FROM Feedback WHERE Waiter_id=%s AND Chef_id=%s AND Dish_name=%s AND Phone=%s AND Time=%s",
            (
                entry["Waiter"],
                entry["Chef"],
                entry["Dish"],
                entry["Phone"],
                entry["Time"],
            ),
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        con.commit()
        print()

    except MySQLError as e:
        con.rollback()
        print("Encountered Database error {!r}, Error number- {}".format(e, e.args[0]))
        print("-" * 10)

    return


def employee_feedback():  # Finds all records in Feedback for given employee
    try:
        employee = input("Enter EmployeeID: ").strip()

        cur.execute(
            "SELECT * FROM Feedback WHERE Waiter_id=%s OR Chef_id=%s",
            (employee, employee),
        )
        rows = cur.fetchall()
        for row in rows:
            print(row)
        con.commit()
        print()

    except MySQLError as e:
        con.rollback()
        print("Encountered Database error {!r}, Error number- {}".format(e, e.args[0]))
        print("-" * 10)

    return


def dish_rating():  # Finds all ratings in Feedback for given dish
    try:
        dish = input("Enter Dish name: ").strip()

        cur.execute("SELECT Rating FROM Feedback WHERE Dish_name=%s", (dish,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        con.commit()
        print()

    except MySQLError as e:
        con.rollback()
        print("Encountered Database error {!r}, Error number- {}".format(e, e.args[0]))
        print("-" * 10)

    return


def avg_emp_rating():  # Finds average rating for given Employee
    try:
        employee = input("Enter Employee ID: ").strip()

        cur.execute(
            "SELECT Avg(Rating) FROM Feedback WHERE Waiter_id=%s OR Chef_id=%s",
            (employee, employee),
        )
        rows = cur.fetchall()
        print(rows)

        # python implementation, to be ignored.
        """
        if len(rows)!=0:
            print("The Average rating for Employee ", employee, " is " , str(sum(rows)//len(rows)))
        else:
            print("Employee not found")
        """

        con.commit()
        print()

    except MySQLError as e:
        con.rollback()
        print("Encountered Database error {!r}, Error number- {}".format(e, e.args[0]))
        print("-" * 10)

    return


def avg_branch_rating():  # Finds average rating for a Branch
    try:
        branch = input("Enter BranchID: ").strip()
        try:
            branch = int(branch)
        except TypeError:
            print("Please enter an integer BranchID")
            raise

        cur.execute(
            "SELECT Avg(Feedback.Rating) FROM Employee INNER JOIN Feedback ON (Employee.Employee_id = Feedback.Waiter_id OR Employee.Employee_id = Feedback.Chef_id) HAVING Employee.Branch_id=%s",
            (branch,),
        )
        rows = cur.fetchall()
        print(rows)

        # python implementation, to be ignored
        """
        rows=[]
        for row in result:
            if row['Branch']==branch:
                rows.append(int(row['Rating']))

        if len(rows)!=0:
            print("The Average rating for Employee ", branch, " is " , str(sum(rows)//len(rows)))
        else:
            print("Branch Feedback not found")
        """

        con.commit()
        print()

    except MySQLError as e:
        con.rollback()
        print("Encountered Database error {!r}, Error number- {}".format(e, e.args[0]))
        print("-" * 10)

    return


def dish_price():  # Updates price of a dish
    try:
        dish = input("Enter Dish name: ").strip()
        price = input("Enter New price: ").strip()

        cur.execute("UPDATE Dish SET Price=%d WHERE Dish_name=%s"(price, dish))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        con.commit()
        print()

    except MySQLError as e:
        con.rollback()
        print("Encountered Database error {!r}, Error number- {}".format(e, e.args[0]))
        print("-" * 10)

    return


# -------------------------------------------------------------------------------
# End of Functionalities


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    if ch == 1:
        get_feedback()
    elif ch == 2:
        employee_feedback()
    elif ch == 3:
        dish_rating()
    elif ch == 4:
        avg_emp_rating()
    elif ch == 5:
        avg_branch_rating()
    elif ch == 6:
        dish_price()
    else:
        print("Error: Invalid Option")


# Global
while 1:
    tmp = sp.call("clear", shell=True)

    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        # Set db name accordingly which have been create by you
        # Set host to the server's address if you don't want to use local SQL server
        con = pymysql.connect(
            host="localhost",
            user=username,
            password=password,
            db="Restaurant_Ratings",
            cursorclass=pymysql.cursors.DictCursor,
            port=5005,
        )
        tmp = sp.call("clear", shell=True)

        if con.open:
            print("Connected")
        else:
            print("Failed to connect")

        tmp = input("Enter any key to CONTINUE>")

        with con.cursor() as cur:
            while 1:
                tmp = sp.call("clear", shell=True)

                print("Enter a number to select corresponding option:-")
                # Queries
                print("0 - Logout")
                print("1 - Get a specific Feedback")  # Select query
                print("2 - Get Feedback for an employee")  # Select query
                print("3 - Get all Ratings for a dish")  # Project query
                print("4 - Get Average rating for an Employee")  # Aggregate query
                print(
                    "5 - Get Average rating for a Branch"
                )  # Analysis - Join and Aggregate
                # Updates
                print("6 - Update the price of a Dish")  # Update

                try:
                    ch = int(input("Enter choice> "))
                except TypeError:
                    print("\nPlease enter an integer\n")
                    raise

                tmp = sp.call("clear", shell=True)
                if ch == 0:
                    break
                else:
                    dispatch(ch)
                    tmp = input("Enter any key to CONTINUE>")

    except:
        tmp = sp.call("clear", shell=True)
        print(
            "Connection Refused: Either username or password is incorrect or user doesn't have access to database"
        )
        tmp = input("Enter any key to CONTINUE>")


# ---------------------------------------------------------------------------------
# redundant features kept for an unassumed requirement later (better safe than sorry :) )
"""
def hireAnEmployee():
    # This is a sample function implemented for the refrence.
    # This example is related to the Employee Database.
    # In addition to taking input, you are required to handle domain errors as well
    # For example: the SSN should be only 9 characters long
    # Sex should be only M or F
    # If you choose to take Super_SSN, you need to make sure the foreign key constraint is satisfied
    # HINT: Instead of handling all these errors yourself, you can make use of except clause to print the error returned to you by MySQL
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


# Functions to check constraints
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
