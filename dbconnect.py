# db 연동에 필요한 패키지 import
import pandas as pd
import cx_Oracle

from main import *

# db 연동


def db():
    cx_Oracle.init_oracle_client(
        lib_dir=r"C:\playdata\oracle\instantclient_19_11")
    connection = cx_Oracle.connect(
        user='ora01', password='oracle_4U2021', dsn='mydb_high')

    cursor = connection.cursor()

    sql = 'INSERT INTO chatbot VALUES (:chatbotName, :rightNow, :loca)'
    cursor.execute(sql, chatbotName=name, rightNow=now, loca=wt.location)

    connection.commit()
    cursor.close()
    connection.close()
