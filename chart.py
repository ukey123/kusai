#!/usr/bin/pythonCGI
# -*- coding: utf-8 -*-
 
from jinja2 import Environment, FileSystemLoader
import sqlite3
import datetime
 
def mychart(environ, start_response):
 
  env = Environment(loader=FileSystemLoader('/home/pi/Desktop/kusai/', encoding='utf8'))
  tpl = env.get_template('template.html')
 
  #テンプレートへ挿入するデータの作成
  title = u"臭いチャート"
 
  temp_list = []
 
  dbpath = '/home/pi/logging'
  connection = sqlite3.connect(dbpath)
  connection.isolation_level = None
  cursor = connection.cursor()
 
  sql = "select datetime(t, 'localtime', '-1 months'), v from kusai"
  #sql = "select strftime('%s' , t), v from kusai where t > datetime('now', '-24 hours')"
  cursor.execute(sql)
  records = cursor.fetchall()
  for record in records:
      temp_list.append({'date':record[0].replace('-',',').replace(' ',',').replace(':',','), 'kusai':record[1]})
    #temp_list.append({'date':record[0].strftime("%Y-%m-%d %H:%M"), 'kusai':record[1]})
  cursor.close()
  connection.close()
 
  #テンプレートへ挿入するデータの作成
  title = u"臭いチャート"
 
  #テンプレートへの挿入
  html = tpl.render({'title':title, 'kusai_list':temp_list})
 
  start_response('200 OK', [('Content-Type', 'text/html')])
  return [html.encode('utf-8')]
 
if __name__ == '__main__':
  from flup.server.fcgi import WSGIServer
  WSGIServer(mychart).run()
