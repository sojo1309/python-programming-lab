# -*- coding: utf-8 -*-
f=open("inntro.txt","r")
contents=f.read() #READS the whole content. contents=f.read(5) reads only the specifed no. of character
print(contents)

#read individual  lines
f=open("inntro.txt","r")
contents=f.readlines()
print(contents)


f=open("inntro.txt","r")
contents=f.readlines()
for x in contents:
 print(x)
