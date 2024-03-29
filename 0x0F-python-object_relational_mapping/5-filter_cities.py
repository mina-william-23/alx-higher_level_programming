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
    searchName = sys.argv[4]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=user_name,
        passwd=password,
        db=database
        )

    mycursor = db.cursor()
    # %s placeholder to avoid sql injection
    query = 'SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC'
    # tuple contain all variables (placeholders)
    query_variable_tuple = (searchName, )

    # execute passed query and tuple to avoid sql injection
    mycursor.execute(query, query_variable_tuple)

    states = [row[0] for row in mycursor.fetchall()]
    result = ", ".join(states)
    print(result)

    mycursor.close()
    db.close()


if __name__ == '__main__':
    connect_grabs()
