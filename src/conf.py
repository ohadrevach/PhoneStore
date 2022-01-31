#!/usr/bin/python
DB_NAME = "../db/store.db"
RAW_DATA = "../db/raw_data.yaml"
PHONE_TABLE = "phone"
SALE_TABLE = "sale"
TABLES = {
   "phone_table": """
   CREATE TABLE phone (
   manufacturer VARCHAR(30),
   model VARCHAR(30),
   price INTEGER,
   quantity INTEGER
   );""",
   "sale_table": """
   CREATE TABLE sale (
   manufacturer VARCHAR(30),
   model VARCHAR(30),
   price INTEGER,
   quantity INTEGER,
   date_of_purchase DATE
   );"""
}
