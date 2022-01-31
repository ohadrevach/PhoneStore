#!/usr/bin/python

import sqlite3
import sys

import src.conf as conf
from src.Phone import Phone
from src.Sale import Sale
import src.db_util as db_utils
import datetime
import os

"""
        In this module I implemented methods that mutual to the objects I created
"""

def connect():
    if not os.path.isfile(conf.DB_NAME):
        path = os.chdir("..")
        os.path.abspath(os.curdir)
    conn = sqlite3.connect(conf.DB_NAME)
    return conn

"""Check if Sale of Phone object is in their tables"""
def isExist(obj, connect, tableName):
    cursor = connect.cursor()

    fmt = "%s='%s'"
    values = ' AND '.join([fmt % (str(name), str(value)) for name, value in obj.parameters.items()])
    try:
        cursor.execute(
            f"SELECT * FROM {tableName} WHERE {values}")

        if cursor.fetchall() == []:
            return False
    except sqlite3.Error as e:
        return False

    return True


"""
    This function insert phone or sale object to their tables
@:object = Phone object or Sale object
@:connect = db connection
@:tableName = The table name we work with
"""

def addToTable(obj, connect, tableName):
    cursor = connect.cursor()
    try:
        cursor.execute(f"INSERT INTO {tableName} VALUES({obj.as_table_value})")

    except sqlite3.Error as e:
        print(f"Error {e.args[0]}")

    # Check if the insertion done
    if tableName == conf.PHONE_TABLE:
        if isExist(obj, connect, tableName) == True:
            connect.commit()  # If the phone inserted well then we save the changes
            print("Added To The Record, check your stock (5 on menu)\n")
        else:
            raise ValueError("Insertion went wrong")

    if tableName == conf.SALE_TABLE:
        if isExist(obj, connect, tableName) == True:
            connect.commit()  # If the phone inserted well then we save the changes
            print("Added To The Record, check sales (6 on menu)\n")
        else:
            db_utils.select_all_by_table(connect, tableName)
            raise ValueError("Insertion went wrong")

    print('\n')


"""
    This function updates the quantity of a specific phone
@:object = Phone object or Sale object
@:connect = db connection
@:tableName = The table name we work with
@:quantity = new quantity of the phone
"""
def updateQuantity(obj, connect, tableName, quantity):
    cursor = connect.cursor()
    cursor.execute(
        f"UPDATE {tableName} SET quantity = '{quantity}' WHERE manufacturer='{obj.manufacturer}' AND model='{obj.model}' AND price='{obj.price}' "
        f"AND IMEI='{obj.IMEI}' AND warranty='{obj.warranty}'")
    obj.setQuantity(quantity)
    # Check the update before commit
    if isExist(obj, connect, tableName):
        connect.commit()  # if it was updated then save the changes
    else:
        raise ValueError("update failed")






"""
    This function shows the stock
@:connect = db connection
@:tableName = phone table name
"""
def phonesInStock(connect, tableName):
    cur = connect.cursor()
    cur.execute(f"SELECT * FROM {tableName} WHERE quantity>0")
    rows = cur.fetchall()
    for row in rows:
        print(row)


"""
    This function returns a list of of sales that been made between dates
@:start_date = Which date to start
@:end_date = Which date to end the search
@:connect = db connection
@:tableName = The Sale tableName
"""
def getSalesByDates(start_date, end_date, connect, tableName):
    cur = connect.cursor()
    cur.execute(f"SELECT * FROM '{tableName}' WHERE date_of_purchase>='{start_date}' AND date_of_purchase<='{end_date}'")
    return cur.fetchall()


"""
This Function delete Sale Of Phone object from their table

@:obj = Sale Or Phone Object
@:connect = db connection
@:tableName = The table name we want to remove from
"""
def deleteFromTable(obj,connect,tableName):
    fmt = "%s='%s'"
    values = ' AND '.join([fmt % (str(name), str(value)) for name, value in obj.parameters.items()])
    cur = connect.cursor()
    if tableName == conf.PHONE_TABLE:
        if not isExist(obj,connect,tableName):
            print("This record is not listed")
            sys.exit(1)
        cur.execute(f"DELETE FROM {tableName} WHERE {values}")
        connect.commit()

    if tableName == conf.SALE_TABLE:
        if not isExist(obj,connect,tableName):
            print("This record is not listed")
            sys.exit(1)
        cur.execute(
            f"DELETE  FROM '{tableName}' WHERE {values}")
        connect.commit()



#-------------------------------------------MENU------------------------------------------------------#
"""
@:data = IMEI as string
This function return if the IMEI is valid
"""
def checkIMEI(data):
    if len(data) < 15:
        return False
    for i in data:
        if i.isdigit() == 0:
            return False
    return True

"""Create and insert Phone object to its table by user input"""
def createPhone(connect):
    man = str(input("Enter manufacturer: "))
    while len(man) > 30 or len(man) == 0:
        man = str(input("Bad input, try another: "))

    model = str(input("Enter Model: "))
    while len(model) > 30 or len(model) == 0:
        model = str(input("Bad input, try another: "))

    price = int(input("Enter Price: "))
    quantity = int(input("Enter quantity: "))
    IMEI = str(input("Enter IMEI(15 digits): "))
    while checkIMEI(IMEI) == False:
        IMEI = str(input("Bad input, Enter IMEI(15 digits): "))
    IMEI = int(IMEI)

    warranty = int(input("Enter how many years of warranty: "))

    phone = Phone(man, model, price, quantity, IMEI, warranty)
    addToTable(phone, connect, conf.PHONE_TABLE)


"""
@:data = date in format day-month-year as string
Check the date format
"""
def checkDate(data):
    try:
        datetime.datetime.strptime(data, '%d-%m-%Y')
    except ValueError:
        return False
    return True

"""Create and insert Sale Object to its table by user input"""
def createSale(connect):
    man = str(input("Enter manufacturer: "))
    while len(man) > 30 or len(man) == 0:
        man = str(input("Too long name, try another: "))

    model = str(input("Enter Model: "))
    while len(model) > 30 or len(model) == 0:
        model = str(input("Too long name, try another: "))

    price = int(input("Enter Price: "))
    quantity = int(input("Enter quantity: "))
    date = str(input("Enter date in this format: day-month-year "))
    while(checkDate(date) == False):
        date = str(input("Enter date in this format: day-month-year "))
    discount = int(input("Enter the discount (if there is no discount insert 0): "))
    sale = Sale(man, model, price, quantity, date, discount)
    addToTable(sale, connect, conf.SALE_TABLE)

# Choice = 2 updating the quantity
def func2(connect):
    man = str(input("Enter manufacturer: "))
    while len(man) > 30 or len(man) == 0:
        man = str(input("Bad input, try another: "))

    model = str(input("Enter Model: "))
    while len(model) > 30 or len(model) == 0:
        model = str(input("Bad input, try another: "))

    quantity = int(input("Enter the new quantity: "))

    price = int(input("Enter Price: "))
    cur = connect.cursor()
    cur.execute(
        f"UPDATE {conf.PHONE_TABLE} SET quantity = '{quantity}' WHERE  model = '{model}' AND manufacturer ='{man}' AND price='{price}'")

    cur.execute(
        f"SELECT * FROM '{conf.PHONE_TABLE}' WHERE model ='{model}' AND quantity='{quantity}' AND manufacturer = '{man}' AND price='{price}'")
    if cur.fetchall() == []:
        raise ValueError("The update has failed")
        exit(1)

    connect.commit()


# Choice = 5 return the amount of sales between dates
def func5(connect):
    date1 = str(input("Enter date from: dd-mm-year"))
    while(checkDate(date1) == False):
        print("Bad input !")
        date1 = str(input("Enter date from: dd-mm-year: "))

    date2 = str(input("Enter date to: dd-mm-year"))
    while(checkDate(date2) == False):
        print("Bad input !")
        date2 = str(input("Enter date to: dd-mm-year"))

    amount = getSalesByDates(date1, date2, connect, conf.SALE_TABLE)
    sums = sum([i[3] for i in amount])
    print(f"Total amount of sales between {date1} to {date2} is: {sums}")



"""Menu function"""
def menu(connect):
    print("Welcome !")

    choices = {

        1: {'func': createPhone, 'args': [connect], 'help': 'Add new phone to the record'},
        2: {'func': func2, 'args': [connect], 'help': 'Update phone quantity'},
        3: {'func': createSale, 'args': [connect], 'help': 'Add a new sale'},
        4: {'func': phonesInStock, 'args': [connect, conf.PHONE_TABLE], 'help': 'Display all phones in stock'},
        5: {'func': func5, 'args': [connect], 'help': 'Display how much sales been made between dates'},
        6: {'func': db_utils.select_all_by_table, 'args': [connect, conf.SALE_TABLE], 'help': 'Display Sales'},

    }

    while True:

        print("Choose one of the options: ")

        for option_num, option in choices.items():
            print(f'\t{option_num}.{option["help"]}')

        choice = int(input("Enter your choice please, 0 to exit: "))

        while choice != 0 and choice not in choices:
            choice = int(input("Bad input, try again please: "))

        if choice == 0:
            print("Good Bye!")
            break

        chs = choices[choice]

        chs['func'](*chs['args'])