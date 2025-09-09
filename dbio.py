"""
dbio.py
"""
import pymysql
import cryptography
import time
import databaseconfig as cfg


class DbIO:
    def __init__(self):
        # Setup connection to DB
        try:
            self.db = pymysql.connect(host=cfg.mysql["host"], user=cfg.mysql["user"], password=cfg.mysql["passwd"], db=cfg.mysql["db"])
        except ImportError:
            raise ValueError("Database configuration not found. Please create databaseconfig.py from databaseconfig.py.example")

        # Establish DB cursor used for write/read activities
        self.cursor = self.db.cursor()

        # ID needs to be removed. This is a temp measure to have unique private keys.
        self.id = 0
        print('dbio object created')

    def write_datapoint_record(self, ticker, sentiment, text):
        # Use parameterized query to prevent SQL injection
        sql = "INSERT INTO datapoint(ID, TICKER, DATE, SENTIMENT, TEXT) VALUES (%s, %s, %s, %s, %s)"
        try:
            self.cursor.execute(sql, (self.id, ticker, time.strftime('%Y-%m-%d %H:%M:%S'), sentiment, text))
            self.db.commit()
            self.id += 1
        except Exception as e:
            self.db.rollback()
            print(f"Error: db rolled back - {e}")

    def read_datapoint_record(self, id):
        # Use parameterized query to prevent SQL injection
        sql = "SELECT * FROM datapoint WHERE id = %s"
        
        try:
            self.cursor.execute(sql, (id,))
            results = self.cursor.fetchall()
            for row in results:
                record_id = row[0]
                ticker = row[1]
                date = row[2]
                sentiment = row[3]
                text = row[4]
                # Uncomment to print results
                # print(f"id: {record_id}, ticker: {ticker}, date: {date}, sentiment: {sentiment}, text: {text}")
            return results
        except Exception as e:
            print(f"Error: unable to fetch data - {e}")
            return None

    def __del__(self):
        self.db.close()
