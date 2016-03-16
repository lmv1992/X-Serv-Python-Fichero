#!/usr/bin/python
# -*- coding: utf-8 -*-
diccionario = {}
fichero=open('/etc/passwd','r')
lineas = fichero.readlines()
for linea in lineas:
	user = linea.split(':')[0] 
	shell = linea.split(':')[-1][:-1]
	diccionario[user] = shell			
fichero.close

for usuarios in diccionario:
	print usuarios,diccionario[usuarios]

try:
	print "\n",diccionario["root"],"\n",diccionario["imaginario"]
except KeyError:
	print "\n","error con el nombre de la clave"	
