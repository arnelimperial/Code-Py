#!/usr/bin/env python3
from time import strftime
import os, sys
def prog_one():
    sel = "(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n(5) Quit"
    h = ":::"
    counter = 100
    var = 0
    a_stop = (1,2,3,4,5)
    
    v = "No default notebook was found, created one."
    z = "Now using file"
    k = "No notebook with that name detected, created one."

    try:
        with open("notebook.txt") as items1:
            items1.read()

            if os.path.exists("notebook.txt") == True:
                print(z, items1.name)
                print(sel +'\n')
                items = int(input("Please select one:"))
                
    except OSError:
        print(v)
        try:
            with open("notebook.txt", "w") as items1:
                if os.path.exists("notebook.txt") == True:
                    print(z, items1.name)
                    print(sel +'\n')
                    items = int(input("Please select one:"))
        except OSError:
            print(v)       
         
    while items < counter:
        var += 1
        if items == 1:
            
            items1 = open("notebook.txt", "a")
            items1.close()
            items1 = open("notebook.txt", "r")
            notewrite2 = items1.read()
            print(notewrite2)
            items1.close()
            print("\n"+ z, items1.name)
            print(sel+'\n')
            items = int(input("Please select one:"))
        elif items == 2:
            container = input("Write a new note:")
            print(z,items1.name)
            print(sel+'\n')
            with open("notebook.txt", "a") as items1:
                notewrite2 = items1.write(container+h+strftime(' %X %x ')+"\n")
                items = int(input("Please select one:"))
        elif items == 3:
            print("Notes deleted.")
            print(sel+'\n')
            items = int(input("Please select one:"))
            items1 = open("notebook.txt", "w")
            items1.close()
        elif items == 4:
            try:
                items_name = input("Give the name of the new file:")
                with open(items_name) as items3:
                    items3.read()
                    if os.path.exists(items_name) == True:
                        print(z, items_name)
                        print(sel+'\n')
                        items2 = int(input("Please select one:"))
                
            except Exception:
                print(k)
                try:
                    with open(items_name, "w") as items3:
                        if os.path.exists(items_name) == True:
                            print(z, items3.name)
                            print(sel+'\n')
                            items2 = int(input("Please select one:"))
                            
                except Exception:
                    print(k)
                
            while True:
                if items2 == 1:
                    items3 = open(items_name, "a")
                    items3.close()
                    items3 = open(items_name, "r")
                    notewrite3 = items3.read()
                    print(notewrite3)
                    items3.close()
                    print("\n"+ z, items3.name)
                    print(sel+'\n')
                    items2 = int(input("Please select one:"))
                elif items2 == 2:
                    container1 = input("Write a new note:")
                    print(z,items3.name)
                    print(sel+'\n')
                    with open(items_name, "a") as items3:
                        notewrite3 = items3.write(container1+h+strftime(' %X %x ')+"\n")
                        items2 = int(input("Please select one:"))
                elif items2 == 3:
                    print("Notes deleted.")
                    print(sel+'\n')
                    items2 = int(input("Please select one:"))
                    items3 = open(items_name, "w")
                elif items2 == 4:
                    try:
                        items_name = input("Give the name of the new file:")
                        with open(items_name) as items3:
                            items3.read()
                            if os.path.exists(items_name) == True:
                                print(z, items_name)
                                print(sel+'\n')
                                items2 = int(input("Please select one:"))
                
                    except Exception:
                        print(k)
                        try:
                            with open(items_name, "w") as items3:
                                if os.path.exists(items_name) == True:
                                    print(z, items3.name)
                                    print(sel+'\n')
                                    items2 = int(input("Please select one:"))
                        except Exception:
                            print(k)
                elif items2 == 5:
                    print("Notebook shuttingdown, thank you.")
                    sys.exit(0)
                else:
                    print("Incorrect selection.")
                    print(sel)
                    items2 = int(input("Please select one:"))
                
                
    
        elif items == 5:
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
