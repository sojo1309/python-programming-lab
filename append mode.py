# -*- coding: utf-8 -*-
f=open("inntro.txt","a")
for i in range(2):
    f.write("Appended line%d\r\n"%(i+1))
    