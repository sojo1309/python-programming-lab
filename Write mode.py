# -*- coding: utf-8 -*-

#Write 1-20 in a new file
my_file=open("num.txt","w+")
for x in range(1,21):
    x=str(x)
    my_file.write(x)
    my_file.write("\n")