#!/usr/bin/python

"""Integration test with pytest testing framework"""
import sqlite3

import pytest
from src.Sale import Sale
from src.Phone import Phone
import src.Methods as mt
import src.conf as conf


"""For every test I will remove the insertions after the test will be completed"""
def test_isExist():
    conn = sqlite3.connect(conf.DB_NAME)
    phone = Phone("LG","20",2500,2,78467327898374,1) # This is not in the DB
    assert mt.isExist(phone,conn,conf.PHONE_TABLE) == False
    mt.addToTable(phone,conn,conf.PHONE_TABLE)
    assert mt.isExist(phone, conn, conf.PHONE_TABLE) == True
    mt.deleteFromTable(phone,conn,conf.PHONE_TABLE)
    assert mt.isExist(phone, conn, conf.PHONE_TABLE) == False


    sale = Sale("iphone", "32", 2452, 2, "11-12-2021", 0)
    assert mt.isExist(sale, conn, conf.SALE_TABLE) == False
    mt.addToTable(sale,conn,conf.SALE_TABLE)
    assert mt.isExist(sale,conn,conf.SALE_TABLE) == True
    mt.deleteFromTable(sale,conn,conf.SALE_TABLE)
    assert mt.isExist(sale, conn, conf.SALE_TABLE) == False

def test_addPhone():
    conn = mt.connect()
    phone = Phone("iphone","x",2500,2,78467857898374,3)
    mt.addToTable(phone,conn,conf.PHONE_TABLE)
    assert mt.isExist(phone,conn,conf.PHONE_TABLE) == True
    phone2 = Phone("one_plus","10",2500,2,78567857264374,2)
    mt.addToTable(phone2,conn,conf.PHONE_TABLE)
    assert mt.isExist(phone2, conn, conf.PHONE_TABLE) == True

    mt.deleteFromTable(phone,conn,conf.PHONE_TABLE)
    assert mt.isExist(phone, conn, conf.PHONE_TABLE) == False
    mt.deleteFromTable(phone2, conn, conf.PHONE_TABLE)
    assert mt.isExist(phone2, conn, conf.PHONE_TABLE) == False

def test_addSale():
    conn = mt.connect()
    sale = Sale("iphone","12",2452,2,"11-12-2021",0)
    mt.addToTable(sale, conn, conf.SALE_TABLE)
    assert mt.isExist(sale, conn, conf.SALE_TABLE) == True
    sale2 = Sale("iphone", "4", 2452, 2, "13-12-2021", 20)
    mt.addToTable(sale2, conn, conf.SALE_TABLE)
    assert mt.isExist(sale2, conn, conf.SALE_TABLE) == True

    mt.deleteFromTable(sale,conn,conf.SALE_TABLE)
    assert mt.isExist(sale, conn, conf.SALE_TABLE) == False
    mt.deleteFromTable(sale2, conn, conf.SALE_TABLE)
    assert mt.isExist(sale2, conn, conf.SALE_TABLE) == False


def test_updateQuantity():
    conn = mt.connect()
    phone = Phone("iphone", "x", 2500, 2, 78467857898374, 3)
    mt.addToTable(phone,conn,conf.PHONE_TABLE)
    assert mt.isExist(phone, conn, conf.PHONE_TABLE) == True
    mt.updateQuantity(phone,conn,conf.PHONE_TABLE,6)
    assert mt.isExist(phone,conn,conf.PHONE_TABLE) == True
    assert phone.quantity == 6
    mt.updateQuantity(phone, conn, conf.PHONE_TABLE, 2)
    assert mt.isExist(phone, conn, conf.PHONE_TABLE) == True
    assert phone.quantity == 2

    mt.deleteFromTable(phone,conn,conf.PHONE_TABLE)
    assert mt.isExist(phone,conn,conf.PHONE_TABLE) == False



