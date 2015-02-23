import csv
import sqlite3

__author__ = 'jster727'


def load_course_database(db_name, csv_filename):
    with open(csv_filename) as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            conn = sqlite3.connect(db_name)
            with conn:
                cur = conn.cursor()
                sql_cmd = "insert into coursedata values(?, ?, ?, ?, ?, ?, ?)"
                cur.execute(sql_cmd, (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))