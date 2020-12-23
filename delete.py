# coding: utf-8

import sqlite3

dbpath = 'logging'
connection = sqlite3.connect(dbpath)
connection.isolation_level = None
cursor = connection.cursor()
sql = "DELETE FROM kusai"
cursor.execute(sql)
connection.commit()
connection.close()
