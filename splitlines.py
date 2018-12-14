# -*- coding: utf-8 -*-

with open("inntro.txt","r") as f:
    data=f.readlines()
    print (data)
    for line in data:
        words=line.split()
        print(words)
    
        