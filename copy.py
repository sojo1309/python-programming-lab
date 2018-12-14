# -*- coding: utf-8 -*-

with open("inntro.txt", "r") as f:
    with open("inntro1.txt", "w") as f1:
        for line in f:
            f1.write(line) 
