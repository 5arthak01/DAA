#!/usr/bin/env python3

import subprocess as sp
import pymysql
import pymysql.cursors
from pymysql import MySQLError
from prettytable import PrettyTable

"""
Functions for different options
"""


def get_feedback():  # Finds specific record in Feedback
    entry = {}
    print("Enter the Feedback details:- ")
    entry["Waiter"] = input("Waiter ID: ").strip()
    entry["Chef"] = input("Chef ID: ").strip()
    entry["Dish"] = input("Dish name: ").strip()
    entry["Phone"] = input("Phone: ").strip()
    entry["Entry_time"] = input("Time as YYYY-MM-DD HH:MM:SS ").strip()

    t = PrettyTable(
        [
            "Waiter_id",
            "Chef_id",
            "Dish_name",
            "Phone",
            "Entry_time",
            "Suggestion",
            "Rating",
        ]
    )

    cur.execute(
        "SELECT * FROM Feedback WHERE Waiter_id=%s AND Chef_id=%s AND Dish_name=%s AND Phone=%s AND Entry_time=%s",
        (
            entry["Waiter"],
            entry["Chef"],
            entry["Dish"],
            entry["Phone"],
            entry["Entry_time"],
        ),
    )
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def employee_feedback():  # Finds all records in Feedback for given employee
    employee = input("Enter EmployeeID: ").strip()
    t = PrettyTable(
        [
            "Waiter_id",
            "Chef_id",
            "Dish_name",
            "Phone",
            "Entry_time",
            "Suggestion",
            "Rating",
        ]
    )
    cur.execute(
        "SELECT * FROM Feedback WHERE Waiter_id=%s OR Chef_id=%s",
        (employee, employee),
    )
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def dish_rating():  # Finds all ratings in Feedback for given dish
    dish = input("Enter Dish name: ").strip()
    t = PrettyTable(["Rating"])
    cur.execute("SELECT Rating FROM Feedback WHERE Dish_name=%s", (dish,))
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def avg_emp_rating():  # Finds average rating for given Employee
    employee = input("Enter Employee ID: ").strip()
    t = PrettyTable(["Average Rating"])
    cur.execute(
        "SELECT Avg(Rating) FROM Feedback WHERE Waiter_id=%s OR Chef_id=%s",
        (employee, employee),
    )
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def employee_super():  # Finds the supervisor of an Employee
    emp = input("Enter Employee ID: ").strip()
    t = PrettyTable(["Supervisor ID"])
    cur.execute("SELECT Super_id from Employee where Employee_id=%s", (emp,))
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def employees_less_than_x():  # Employees with average rating less than given number 'x'
    x = input("Enter x: ").strip()
    try:
        x = float(x)
    except ValueError:
        print("Please enter a valid number")
        return

    t = PrettyTable(["Employee Id", "Average Rating"])
    cur.execute(
        "SELECT Employee.Employee_id,Avg(Feedback.Rating) FROM Employee INNER JOIN Feedback ON (Employee.Employee_id = Feedback.Waiter_id OR Employee.Employee_id=Feedback.Chef_id) group by Employee_id having Avg(Feedback.Rating)<%s",
        (x,),
    )
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def max_min_dish_rating():  # Finds minimum or maximum rating for given Dish
    choice = input(
        "Enter 'Min' or 'Max' for Minimum or Maximum rating respectively: "
    ).strip()

    if choice == "Max" or choice == "Min":
        dish = input("Enter Dish name: ").strip()
        cur.execute(
            f"SELECT {choice}(Rating) from Feedback where Dish_name=%s", (dish,)
        )
    else:
        print("Invalid Input")
        return
    t = PrettyTable([f"{choice} Rating"])
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()

    return


def update_dish_price():  # Updates price of a dish
    dish = input("Enter Dish name: ").strip()
    price = input("Enter New price: ").strip()
    try:
        price = int(price)
    except ValueError:
        print("Please enter a valid number for the Price")
        return

    cur.execute("UPDATE Dish SET Price=%s WHERE Dish_name=%s", (price, dish))
    con.commit()
    print()

    return


def search_suggestion():  # Partial Matching in Suggestions from Feedback
    search = input("Enter what you are searching for: ").strip()
    query = """SELECT Suggestion FROM Feedback WHERE Suggestion LIKE %s"""
    t = PrettyTable(["Suggestion"])
    cur.execute(query, ("%" + search + "%",))
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def get_subordinate():  # Gives Subordinates of Manager
    manager = input("Enter the Manager ID: ").strip()
    t = PrettyTable(["Employee ID"])
    cur.execute("SELECT Employee_id FROM Employee where Super_id = %s", (manager,))
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def insert_employee():  # Add an Employee
    employee = input("Enter New Employee ID: ").strip()
    branch = input("Enter Branch ID: ").strip()
    supervisor = input("Enter Supervisor ID: ").strip()
    restaurant = input("Enter Restaurant cin number: ").strip()

    cur.execute(
        "INSERT INTO Employee (Employee_id, Branch_id, Super_id, Res) VALUES (%s, %s, %s, %s)",
        (employee, branch, supervisor, restaurant),
    )
    con.commit()
    print()

    return


def insert_branch():  # Add a Branch
    restaurant = input("Enter Restaurant cin number: ").strip()
    branch = input("Enter New Branch ID: ").strip()

    cur.execute(
        "INSERT INTO Branch (Res, Branch_id) VALUES (%s, %s)", (restaurant, branch)
    )
    con.commit()
    print()

    return


def insert_restaurant():  # Add a Restaurant
    restaurant = input("Enter New Restaurant Name: ").strip()
    cin = input("Enter New Restaurant cin number: ").strip()

    cur.execute(
        "INSERT INTO Restaurant (cin_num, name) VALUES (%s, %s)", (cin, restaurant)
    )
    con.commit()
    print()

    return


def insert_feedback():  # Add a Feedback
    waiter = input("Enter Waiter ID: ").strip()
    chef = input("Enter Chef ID: ").strip()
    dish = input("Enter Dish Name: ").strip()
    phone = input("Enter Phone Number: ").strip()
    entry = input("Enter Entry Time as YYYY-MM-DD HH:MM:SS: ").strip()
    suggestion = input("Enter Suggestion: ").strip()
    rating = input("Enter Rating: ").strip()

    cur.execute(
        "INSERT INTO Customers (Phone, Entry_time) VALUES (%s, %s)", (phone, entry)
    )
    cur.execute(
        "INSERT INTO Feedback (Waiter_id, Chef_id, Dish_name, Phone, Entry_time, Suggestion, Rating) VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (waiter, chef, dish, phone, entry, suggestion, rating),
    )
    con.commit()
    print()

    return


def avg_dish_and_customer_ratings():  # Gives Average Rating of Dish and Average Rating by a Customer
    print("Enter a number to select corresponding option:-")
    print("1 - Get the average Rating of a Dish")
    print("2 - Get the average Rating given by a Customer")
    choice = input().strip()
    if choice == "1":
        choice = "Dish_name"
        inp = input("Enter the Dish name: ").strip()
    elif choice == "2":
        choice = "Phone"
        inp = input("Enter the Phone number of the Customer: ").strip()
    else:
        print("Invalid Input")
        return
    t = PrettyTable(["Average Rating"])
    cur.execute(f"SELECT AVG(Rating) FROM Feedback WHERE {choice}=%s", (inp,))
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def avg_rating_branch_and_restaurant():  # Finds average rating for a Branch
    print("Enter a number to select corresponding option:-")
    print("1 - Get the average Rating of a Restaurant")
    print("2 - Get the average Rating of a Branch")
    choice = input().strip()
    if choice == "1":
        choice = "Res"
        inp = input("Enter the Restaurant cin number: ").strip()
    elif choice == "2":
        choice = "Branch_id"
        inp = input("Enter the Branch_Id: ").strip()
    else:
        print("Invalid Input")
        return

    t = PrettyTable(["Average Rating"])
    cur.execute(
        f"SELECT Avg(Feedback.Rating) FROM Employee INNER JOIN Feedback ON (Employee.Employee_id = Feedback.Waiter_id OR Employee.Employee_id = Feedback.Chef_id) WHERE Employee.{choice}=%s",
        (inp,),
    )
    rows = cur.fetchall()
    for row in rows:
        t.add_row(row.values())
    print(t)
    con.commit()
    print()

    return


def delete_dish():  # Delete a Dish
    dish = input("Enter Dish to be Deleted: ").strip()

    cur.execute("DELETE FROM Dish_meal WHERE Dish_name = %s", (dish))
    cur.execute("DELETE FROM Feedback WHERE Dish_name = %s", (dish))
    cur.execute("DELETE FROM Dish WHERE Dish_name = %s", (dish))
    con.commit()
    print()

    return


def max_min_employee_rating_given_branch():  # Get Maximum or Minimum Rated Employee for a Branch
    choice = input(
        "Enter 'Min' or 'Max' for Minimum or Maximum rating respectively: "
    ).strip()

    choice_dict = {"Max": 0, "Min": 1}
    if choice == "Max" or choice == "Min":
        branch = input("Enter Branch: ").strip()
        t = PrettyTable(["Employee ID", "Average Rating"])
        cur.execute(
            "SELECT Employee.Employee_id, Avg(Feedback.Rating) FROM Employee INNER JOIN Feedback ON (Employee.Employee_id = Feedback.Waiter_id OR Employee.Employee_id=Feedback.Chef_id) WHERE Employee.Branch_id = %s group by Employee.Employee_id",
            (branch,),
        )
        rows = cur.fetchall()
        max = 0 if choice == "Max" else 11
        counter = 0
        pointer = 0
        for row in rows:
            if (row["Avg(Feedback.Rating)"] > max) ^ choice_dict[choice]:
                pointer = counter
                max = row["Avg(Feedback.Rating)"]
            counter += 1
        for i in rows:
            if i["Avg(Feedback.Rating)"] == max:
                t.add_row(i.values())
        print(t)
        con.commit()
        print()

    else:
        print("Invalid Input")

    return


# -------------------------------------------------------------------------------
# End of Functionalities


def dispatch(ch):
    """
    Function that maps helper functions to option entered
    """
    try:
        if ch == 1:
            get_feedback()
        elif ch == 2:
            employee_feedback()
        elif ch == 3:
            dish_rating()
        elif ch == 4:
            avg_emp_rating()
        elif ch == 5:
            avg_rating_branch_and_restaurant()
        elif ch == 6:
            max_min_dish_rating()
        elif ch == 7:
            employee_super()
        elif ch == 8:
            employees_less_than_x()
        elif ch == 9:
            search_suggestion()
        elif ch == 10:
            get_subordinate()
        elif ch == 11:
            avg_dish_and_customer_ratings()
        elif ch == 12:
            max_min_employee_rating_given_branch()
        elif ch == 21:
            update_dish_price()
        elif ch == 22:
            insert_employee()
        elif ch == 23:
            insert_branch()
        elif ch == 24:
            insert_restaurant()
        elif ch == 25:
            insert_feedback()
        elif ch == 26:
            delete_dish()
        else:
            print("Error: Invalid Option")
    except MySQLError as e:
        con.rollback()
        print("\n\n" + "-" * 20)
        print(
            " Encountered database error.\n Error number {} - {}".format(
                e.args[0], e.args[1]
            )
        )
        print("-" * 20 + "\n\n")


# Global
while 1:
    tmp = sp.call("clear", shell=True)

    # Can be skipped if you want to hard core username and password
    username = input("Username: ")
    password = input("Password: ")

    try:
        con = pymysql.connect(
            host="localhost",  # OR set appropriate host
            user=username,
            password=password,
            db="Restaurant_Ratings",  # Name of our Database
            cursorclass=pymysql.cursors.DictCursor,
            port=5005,  # Since our docker container hosts mysql server at this port
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
                print(
                    "5 - Get Average rating for a Branch or Restaurant"
                )  # Analysis - Join and Aggregate
                print(
                    "6 - Get the Maximum or Minimum rating of a particular dish"
                )  # Analysis - Join and Aggregate
                print("7 - Get the Supervisor of a Particular Employee")  # Select
                print(
                    "8 - Get Employees whose average rating is less than a given value X"
                )  # Analysis - Join and Aggregate
                print("9 - Search using a partial match in suggestion")  # Search
                print("10 - Get all subordinates of a Particular Manager")  # Select
                print(
                    "11 - Get the average rating of a dish or the average rating given by a customer"
                )  # Aggregate
                print(
                    "12 - Get Highest and Lowest Rated Employees of a Given Branch"
                )  # Analysis - Join and Aggregate

                print()
                # Updates
                print("21 - Update the price of a Dish")  # Update
                print("22 - Add an Employee")  # Insertion
                print("23 - Add a Branch")  # Insertion
                print("24 - Add a Restaurant")  # Insertion
                print("25 - Add a Feedback")  # Insertion
                print("26 - Delete a Dish")  # Delete

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
        print(
            "Connection Refused: Either username or password is incorrect or user doesn't have access to database"
        )
        tmp = input("Enter any key to CONTINUE>")
