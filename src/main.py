#!/usr/bin/python
import sqlite3
import sys
import src.db_util as db_utils
import src.conf as conf
import os.path
import src.Methods as mt
import logging
import TestUnit

if __name__ == '__main__':
    connection = None

    sales_logger = logging.getLogger('sales_server')
    sales_logger.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    fch = logging.FileHandler('mylog.log')
    fch.setLevel(logging.DEBUG)

    sales_logger.addHandler(ch)
    sales_logger.addHandler(fch)

    try:
        connection = db_utils.create_db()

        cur = connection.cursor()
        cur.execute(f"SELECT * FROM {conf.PHONE_TABLE}")
        rows = cur.fetchall()

        if len(rows) == 0: #If the Db file not exist then load the raw data file and add cols
            db_utils.load_raw_data(connection)
            cur.execute(f"ALTER TABLE {conf.PHONE_TABLE} ADD IMEI BIGINT DEFAULT '123456789012345' ")
            cur.execute(f"ALTER TABLE {conf.PHONE_TABLE} ADD warranty INTEGER DEFAULT '0'")
            cur.execute(f"ALTER TABLE {conf.SALE_TABLE} ADD discount INTEGER DEFAULT '0'")

        mt.menu(connection)

    # db_utils.select_all_by_table(connection, conf.PHONE_TABLE)
    # db_utils.select_all_by_table(connection, conf.SALE_TABLE)
    except sqlite3.Error as sql_err:
        sales_logger.error(f"sqlite3.Error {sql_err}")
    except ValueError as val_err:
        sales_logger.error(f"ValueError {val_err}")
    finally:
        if connection:
            connection.close()
