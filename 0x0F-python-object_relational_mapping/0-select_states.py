#!/usr/bin/python3
'''
 script that lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys


def connect_grabs():
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user_name,
        passwd=password,
        db=database
        )

    mycursor = db.cursor()
    mycursor.execute('SELECT * FROM states ORDER BY id ASC')
    data = mycursor.fetchall()
    for row in data:
        print(row)

    mycursor.close()
    db.close()


if __name__ == '__main__':
    connect_grabs()
