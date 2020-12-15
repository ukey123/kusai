#!/usr/bin/pythonCGI
# -*- coding: utf-8 -*-
 
from jinja2 import Environment, FileSystemLoader
import sqlite3
import datetime
 
def mychart(environ, start_response):
 
 
  #テンプレートへ挿入するデータの作成
  title = u"Kusai Chart"
 
  temp_list = []
 
  dbpath = '/home/pi/logging'
  connection = sqlite3.connect(dbpath)
  connection.isolation_level = None
  cursor = connection.cursor()
 
  sql = "select * from kusai "
  #sql = "select * from kusai where strftime('%s',datetime(t, '+24 hours')) > datetime('now')"
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    print(record[0], record[1])
    #temp_list.append({'date':record[0].strftime("%Y-%m-%d %H:%M"), 'kusai':record[1]})
  cursor.close()
  connection.close()

mychart(0,0)
