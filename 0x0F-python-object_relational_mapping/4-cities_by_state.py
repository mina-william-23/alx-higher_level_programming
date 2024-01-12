#!/usr/bin/python3
'''
 script that lists all cities from the database hbtn_0e_4_usa
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
    query = 'SELECT cities.id, cities.name, states.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            ORDER BY cities.id ASC'

    # execute passed query
    mycursor.execute(query)

    data = mycursor.fetchall()
    for row in data:
        print(row)

    mycursor.close()
    db.close()


if __name__ == '__main__':
    connect_grabs()
