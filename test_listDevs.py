#!/usr/bin/python

import sqlite3
import json
import sys
import requests
import json, ast
from collections import OrderedDict
import subprocess

conn=sqlite3.connect('mydatabase.db')
c=conn.cursor()
query=c.execute('SELECT * FROM info')
fetch=c.fetchall()
j=[]
for i in fetch:
	j.append(list(i))
s=[]
f=[]
for sublist in j :
	for item in sublist:
		s.append(str(item)) 
		
for j in range(len(s)):
	if s[j]=='None':
		s[j]=''

print(s)


url ='http://localhost:5000/listDevs.php'
response=requests.get(url)
k=[]
data=response.text
a=data.split("|")
for n in a:
	k.append(str(n))
q=[]
for i in k :
	q.append((i.replace('\n','')))
print(q)

if s[:]==q[:-1]:
	print('listDevs.php returned same values as in database')
else:
	print('listDevs.php did not return same values')
	print('listDevs.php failed')


