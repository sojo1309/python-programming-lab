# -*- coding: utf-8 -*-
num_words = 0
with open("inntro.txt", "r") as f:
    for line in f:
        words=line.split ()
        num_words += len (words)
print("Number of words:") 
print(num_words)