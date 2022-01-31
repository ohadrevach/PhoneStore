import unittest
from src.Sale import Sale
from src.Phone import Phone
import src.Methods as mt
import sqlite3
import src.conf as conf
import os.path

"""Unit Testing"""


class TestSystem(unittest.TestCase):

    def test_isExist(self):
        conn = sqlite3.connect(conf.DB_NAME)
        phone = Phone("LG", "20", 2500, 2, 78467327898374, 1)  # This is not in the DB
        self.assertFalse(mt.isExist(phone, conn, conf.PHONE_TABLE))
        mt.addToTable(phone, conn, conf.PHONE_TABLE)
        self.assertTrue(mt.isExist(phone, conn, conf.PHONE_TABLE))
        mt.deleteFromTable(phone, conn, conf.PHONE_TABLE)
        self.assertFalse(mt.isExist(phone, conn, conf.PHONE_TABLE))

        sale = Sale("iphone", "32", 2452, 2, "11-12-2021", 0)
        self.assertFalse(mt.isExist(sale, conn, conf.SALE_TABLE))
        mt.addToTable(sale, conn, conf.SALE_TABLE)
        self.assertTrue(mt.isExist(sale, conn, conf.SALE_TABLE))
        mt.deleteFromTable(sale, conn, conf.SALE_TABLE)
        self.assertFalse(mt.isExist(sale, conn, conf.SALE_TABLE))

    def test_addPhone(self):
        conn = sqlite3.connect(conf.DB_NAME)
        phone = Phone("iphone", "x", 2500, 2, 78467857898374, 3)
        mt.addToTable(phone, conn, conf.PHONE_TABLE)
        self.assertTrue(mt.isExist(phone, conn, conf.PHONE_TABLE))
        phone2 = Phone("one_plus", "10", 2500, 2, 78567857264374, 2)
        mt.addToTable(phone2, conn, conf.PHONE_TABLE)
        self.assertTrue(mt.isExist(phone2, conn, conf.PHONE_TABLE))

        mt.deleteFromTable(phone, conn, conf.PHONE_TABLE)
        self.assertFalse(mt.isExist(phone, conn, conf.PHONE_TABLE))
        mt.deleteFromTable(phone2, conn, conf.PHONE_TABLE)
        self.assertFalse(mt.isExist(phone2, conn, conf.PHONE_TABLE))

    def test_addSale(self):
        conn = sqlite3.connect(conf.DB_NAME)
        sale = Sale("iphone", "12", 2452, 2, "11-12-2021", 0)
        mt.addToTable(sale, conn, conf.SALE_TABLE)
        self.assertTrue(mt.isExist(sale, conn, conf.SALE_TABLE))
        sale2 = Sale("iphone", "4", 2452, 2, "13-12-2021", 20)
        mt.addToTable(sale2, conn, conf.SALE_TABLE)
        self.assertTrue(mt.isExist(sale2, conn, conf.SALE_TABLE))

        mt.deleteFromTable(sale, conn, conf.SALE_TABLE)
        self.assertFalse(mt.isExist(sale, conn, conf.SALE_TABLE))
        mt.deleteFromTable(sale2, conn, conf.SALE_TABLE)
        self.assertFalse(mt.isExist(sale2, conn, conf.SALE_TABLE))

    def test_updateQuantity(self):
        conn = sqlite3.connect(conf.DB_NAME)
        phone = Phone("iphone", "x", 2500, 2, 78467857898374, 3)
        mt.addToTable(phone, conn, conf.PHONE_TABLE)
        mt.updateQuantity(phone, conn, conf.PHONE_TABLE, 6)
        self.assertTrue(mt.isExist(phone, conn, conf.PHONE_TABLE))
        self.assertEqual(phone.quantity,6)
        mt.updateQuantity(phone, conn, conf.PHONE_TABLE, 2)
        self.assertTrue(mt.isExist(phone, conn, conf.PHONE_TABLE))
        self.assertEqual(phone.quantity,2)

        mt.deleteFromTable(phone, conn, conf.PHONE_TABLE)
        self.assertFalse(mt.isExist(phone, conn, conf.PHONE_TABLE))

if __name__ == '__main__':
    unittest.main()

