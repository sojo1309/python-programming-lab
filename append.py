# -*- coding: utf-8 -*-
f=open("inntro.txt","r")
data=f.read()
f.close()
f1=open("inntro1.txt","a")
f1.write(data)
f1.close