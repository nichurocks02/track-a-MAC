#!/usr/bin/python

import sqlite3
import json
import sys
import requests
import json, ast
from collections import OrderedDict
import subprocess

parameters={
	"A":'192.168.184.23',
	"B":'161',	
	"C":'public',
	"D": '2'
	
}

parameters1 = OrderedDict(sorted(parameters.items()))
n= [v for v in parameters1.values()]
url='http://localhost:5000/removeDevice.php'
response = requests.get(url, params=parameters1)
conn=sqlite3.connect('mydatabase.db')
c=conn.cursor()
fquery=c.execute("SELECT EXISTS (SELECT * FROM info WHERE  IP=?)",(parameters['A'],)).fetchall()
if (fquery[0][0])==1:
	print('The device exists in the data base')
	print('please wait while the solution removes the device info')
	ip=subprocess.call(['curl','http://localhost:5000/removeDevice1.php?ip=192.168.184.23&port=161&community=public&version=2'])
else:
	pass


query=c.execute("SELECT NOT EXISTS (SELECT * FROM info WHERE  IP=?)",(parameters['A'],)).fetchall()
if (query[0][0])==1:
	print('\n success')
else:
	print('\n unsuccessfull ')

