#!/usr/bin/pythonCGI
# -*- coding: utf-8 -*-
 
from jinja2 import Environment, FileSystemLoader
import sqlite3
import datetime
 
def mychart(environ, start_response):
 
  env = Environment(loader=FileSystemLoader('./', encoding='utf8'))
  tpl = env.get_template('template.html')
 
  #テンプレートへ挿入するデータの作成
  title = u"Kusai Chart"
 
  temp_list = []
 
  dbpath = 'logging"'
           connection = sqlite3.connect(dbpath)
           connection.isolation_level = None
           cursor = connection.cursor()
 
  sql = "select * from kusai where datetime('now', 'localtime', '+24 HOUR') > datetime('now', 'localtime')"
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
    temp_list.append({'date':record[0].strftime("%Y-%m-%d %H:%M"), 'kusai':record[1]})
  cursor.close()
  connection.close()
 
  #テンプレートへ挿入するデータの作成
  title = u"Kusai Chart"
 
  #テンプレートへの挿入
  html = tpl.render({'title':title, 'temp_list':temp_list})
 
  start_response('200 OK', [('Content-Type', 'text/html')])
  return [html.encode('utf-8')]
 
if __name__ == '__main__':
  from flup.server.fcgi import WSGIServer
  WSGIServer(mychart).run()