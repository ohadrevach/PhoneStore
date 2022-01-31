#!/usr/bin/python

import yaml
import sqlite3
import os.path
import src.conf as conf
import logging

sales_logger = logging.getLogger('sales_server')


def create_db():

    if os.path.isfile(conf.DB_NAME):
        sales_logger.debug("Database exist, skip create")
        return sqlite3.connect(f'file:{conf.DB_NAME}?mode=rw', uri=True)
    else:
        sales_logger.debug("Database does not exist, creating")
        conn = sqlite3.connect(conf.DB_NAME)
        for table in conf.TABLES.values():
            conn.cursor().execute(table)
        return conn


def load_raw_data(conn):
    with open(conf.RAW_DATA) as file:
        records = yaml.load(file, Loader=yaml.FullLoader)
        for key in records.keys():
            for item in records[key]:
                conn.cursor().execute(
                    f"INSERT INTO {key} VALUES({records[key][item]})"
                )
                conn.commit()
                
                
def select_all_by_table(conn, table_name):
    print(f"\nAll data in table:{table_name}")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name}")
    rows = cur.fetchall()
    for row in rows:
        print(row)

