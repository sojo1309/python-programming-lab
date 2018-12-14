# -*- coding: utf-8 -*-
wordsearch=input("enter the word")
k=0
with open("inntro.txt", "r") as f:
    for line in f:
         words = line.split ()
         for i in words:
             if(i== wordsearch ):
                    k=k+1
print("Occurrences of the word: ",k) 