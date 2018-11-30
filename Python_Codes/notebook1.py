#!/usr/bin/env python3

import os, sys
def prog_one():
    sel = "(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit"
    counter = 100
    var = 0
    a_stop = (1,2,3,4)
    print(sel +'\n')
    items = int(input("Please select one:"))
    while items < counter:
        var += 1
        if items == 1:
            
            items1 = open("notebook.txt", "a")
            items1.close()
            items1 = open("notebook.txt", "r")
            notewrite2 = items1.read()
            print(notewrite2.rstrip())
            items1.close()
            print('\n'+sel+'\n')
            items = int(input("Please select one:"))
        elif items == 2:
            container = input("Write a new note:")
            print(sel+'\n')
            items1 = open("notebook.txt", "a")
            notewrite2 = items1.write(container +"\n")
            items1.close()
            items = int(input("Please select one:"))
        elif items == 3:
            print("Notes deleted.")
            print(sel+'\n')
            items = int(input("Please select one:"))
            items1 = open("notebook.txt", "w")
            items1.close()
        elif items == 4:
            print("Notebook shuttingdown, thank you.")
            break
        else:
            try:
                print("Incorrect selection.")
                print(sel)
                items = int(input("Please select one:"))
            except ValueError:
                print("Incorrect selection.")
            except Exception as e:
                print(e)
                

if __name__ == "__main__":
    prog_one()
