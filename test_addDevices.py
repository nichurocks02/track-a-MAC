#!/usr/bin/python3
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
#print(n)
url='http://localhost:5000/addDevices.php'
response = requests.post(url, params=parameters1)
ip=subprocess.call(['curl','http://localhost:5000/addDevice.php?ip=192.168.184.23&port=161&community=public&version=2'])

conn=sqlite3.connect('mydatabase.db')
c=conn.cursor()

query=c.execute("SELECT * FROM info WHERE IP=?",(n[0],))
#print(query)
fetch=c.fetchone()
k=[]
for i in fetch :
	k.append(str(i))

#parameters_list=parameters.values()
#print(k[:4])
#print(type(query))
if n==k[:4]:
	print('succesfull')
else:
	print('unsuccesfull')
	print('\n')
	print('The device you are looking for is not present/added')

conn.close()


