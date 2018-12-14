# -*- coding: utf-8 -*-
f=open("inntro.txt","r")
contents=f.read(5)
print (contents)

#check curret  posiition
position=f.tell()
print("position is",position)

#reposition pointer at the beginning once again
position=f.seek(0,0)
data=f.read(6)
print (data)
position=f.tell()
print(position)

