#!/usr/bin/env python3
prog = input("Give a file name:")
arroz = input("Write something:")

with open(prog, "w") as log1:
    log1.write(arroz)
    print("Wrote ", arroz, "to the file", log1.name)