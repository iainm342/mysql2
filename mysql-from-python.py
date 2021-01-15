import os
import datetime
import pymysql

username = os.getenv('iainm342')

connection = pymysql.connect(host='localhost',
                            user=username,
                            password = '',
                            db='Chinook')

try:
    with connection.cursor() as cursor:
        cursor.execute("""CREATE TABLE IF NOT EXISTS
                        Friends(name char(20), age int, DOB datetime);""")
        # Note that the above will stay display a warning (NOT AN ERROR) if the
        # table already exists
finally:
    connection.close()