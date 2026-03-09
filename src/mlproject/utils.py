import os
import sys
import pandas as pd
import pymysql
from dotenv import load_dotenv

from mlproject.logger import logging
from mlproject.exception import CustomException

load_dotenv()

host = "localhost"
user = "root"
password = "1234"
db = "college"

# database validation
if db is None or db == "":
    raise CustomException("Database not provided", sys)


def read_sql_data():
    logging.info("Reading SQL database started")

    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=db   # better to use 'database'
        )

        logging.info("Connection established")

        df = pd.read_sql_query("SELECT * FROM students", mydb)

        print(df.head())

        mydb.close()

        return df

    except Exception as e:
        raise CustomException(e, sys)