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
        entry["Entry_time"] = input("Time as YYYY-MM-DD HH:MM:SS ").strip()

        cur.execute(
            "SELECT * FROM Feedback WHERE Waiter_id=%s AND Chef_id=%s AND Dish_name=%s AND Phone=%s AND Time=%s",(
                entry["Waiter"],
                entry["Chef"],
                entry["Dish"],
                entry["Phone"],
                entry["Entry_time"],
            )
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
            (employee, employee)
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
            (employee, employee)
        )
        rows = cur.fetchall()
        print(rows)

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
            "SELECT Avg(Feedback.Rating) FROM Employee INNER JOIN Feedback ON (Employee.Employee_id = Feedback.Waiter_id OR Employee.Employee_id = Feedback.Chef_id) WHERE Employee.Branch_id=%s",
            (branch,)
        )
        rows = cur.fetchall()
        print(rows)

        con.commit()
        print()

    except MySQLError as e:
        con.rollback()
        print("Encountered Database error {!r}, Error number- {}".format(e, e.args[0]))
        print("-" * 10)

    return


def employee_super(): # Finds the supervisor of an Employee
    try:
        emp = input("Employee ID: ").strip()
        cur.execute("SELECT Super_id from Employee where Employee_id=%s", (emp,))
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


def employees_less_than_x(): # Employees with average rating less than given number 'x'
    try:
        x = input("Enter x: ").strip()
        try:
            x = int(x)
        except TypeError:
            print("Please enter a natural number")
            raise

        cur.execute(
            "SELECT Employee.Employee_id,Avg(Feedback.Rating) FROM Employee INNER JOIN Feedback ON (Employee.Employee_id = Feedback.Waiter_id OR Employee.Employee_id=Feedback.Chef_id) group by Employee_id having Avg(Feedback.Rating)<%s",
            (x,),
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


def max_min_dish_rating(): # Finds minimum or maximum rating for given Dish
    try:
        choice = input("Enter \'Min\' or \'Max\' for Minimum or Maximum rating respectively: ").strip()
        dish = input("Enter Dish name: ").strip()

        if choice == "Max":
            cur.execute("SELECT MAX(Rating) from Feedback where Dish_name=%s", (dish,))
        elif choice == "Min":
            cur.execute("SELECT MIN(Rating) from Feedback where Dish_name=%s", (dish,))
        else:
            print("Invalid Input")
        
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


def update_dish_price():  # Updates price of a dish
    try:
        dish = input("Enter Dish name: ").strip()
        price = input("Enter New price: ").strip()
        try:
            price = int(price)
        except TypeError:
            print("Please enter a natural number")
            raise

        cur.execute("UPDATE Dish SET Price=%s WHERE Dish_name=%s", (price, dish))
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
        max_min_dish_rating()
    elif ch == 7:
        employee_super() 
    elif ch == 8:
        employees_less_than_x()
    elif ch == 9:
        update_dish_price()
    else:
        print("Error: Invalid Option")


# Global
while 1:
    tmp = sp.call("clear", shell=True)

    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(
            host="localhost", # OR set appropriate host
            user=username,
            password=password,
            db="Restaurant_Ratings", # Name of our Database 
            cursorclass=pymysql.cursors.DictCursor,
            port=5005 # Since our docker container hosts mysql server at this port
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
                print("0 - Logout")
                # Queries
                print("1 - Get a specific Feedback")  # Select 
                print("2 - Get Feedback for an employee")  # Select 
                print("3 - Get all Ratings for a dish")  # Project 
                print("4 - Get Average rating for an Employee")  # Aggregate 
                print("5 - Get Average rating for a Branch")  # Analysis - Join and Aggregate
                print("6 - Get the Maximum or Minimum rating of a particular dish") # Analysis - Join and Agrregate
                print("7 - Get the Supervisor of a Particular Employee") # Select
                print("8 - Get Employees whose average rating is less than a given value X") # Analysis - Join and Agrregate
                # Updates
                print("9 - Update the price of a Dish")  # Update
                
                try:
                    ch = int(input("Enter choice> ").strip())
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
        print("Connection Refused: Either username or password is incorrect or user doesn't have access to database")
        tmp = input("Enter any key to CONTINUE>")
