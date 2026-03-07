import os
import sys
import pandas as pd
import pymysql
from dotenv import load_dotenv

from mlproject.logger import logging
from mlproject.exception import CustomException  # fixed import

load_dotenv()

host="localhost"
user="root"
password="1234"
db="college"
if not db:
    raise CustomException("Database not provided in .env", sys)

def read_sql_data():
    logging.info("Reading SQL database started")

    try:
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )

        logging.info(f"Connection established: {mydb}")

        df = pd.read_sql_query("SELECT * FROM students", mydb)

        print(df.head())

        mydb.close()

        return df

    except Exception as e:
        raise CustomException(e, sys)