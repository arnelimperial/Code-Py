#!/usr/bin/env python3

from time import strftime
import os, sys
import pickle

def prog_one(*args):
    sel = "(1) Read the notebook\n(2) Add note\n(3) Edit a note\n(4) Delete a note\n(5) Save and quit"
    h = ":::"
    counter = 100
    var = 0
    a_stop = (1,2,3,4,5)
    
    things = []
    v = "No default notebook was found, created one."
    z = "Now using file"
    k = "No notebook with that name detected, created one."

    try:
        
        with open('notebook.dat', 'rb') as items1:
            pickle.load(items1)
            if os.path.exists('notebook.dat') == True:
                print(sel +'\n')
                items = int(input("Please select one:"))
    except OSError:
        print(v)
        
        with open('notebook.dat', 'wb') as items1:
            pickle.dump(things, items1)
            print(sel +'\n')
            items = int(input("Please select one:"))
        
        
    while items < counter:
        var += 1
        if items == 1:
            with open("notebook.dat", "rb") as items1:
                files = pickle.load(items1)
                print("".join(files))
                print(sel+'\n')
                items = int(input("Please select one:"))
                

                
        elif items == 2:
            container = input("Write a new note:")
            
            print(sel+'\n')
            things = [container]  
            with open("notebook.dat", "wb") as items1:
                pickle.dump(things+[h+strftime(' %X %x ')], items1)
                items = int(input("Please select one:"))
                  
        elif items == 4:
            things = [args]  
            print("The list has {} notes.". format(len(things)))
            change2 = int(input("Which of them will be deleted?:"))
            try:
                with open("notebook.dat", "rb") as items1:
                    files = pickle.load(items1)
                    x = files.pop(0)
                
                
            except IndexError as e:
                print(e)
                items = int(input("Please select one:"))
            else:
                print("Deleted note", "".join(x)+h+strftime(' %X %x '))
                things = []
                with open("notebook.dat", "wb") as items1:
                   pickle.dump(things, items1)
                   print(sel+'\n')
                   items = int(input("Please select one:"))
                   
        elif items == 3:
            print("The list has {} notes.". format(len(things)))
            change = int(input("Which of them will be changed?:"))
            try:
                with open("notebook.dat", "rb") as items1:
                     files = pickle.load(items1)
                     things.pop(change)
                
            except IndexError as e:
                print(e)
                items = int(input("Please select one:"))
            else:
                print("".join(files))
                container = input("Give the new note:")
                things = [container]
                with open("notebook.dat", "wb") as items1:
                    pickle.dump(things+[h+strftime(' %X %x ')], items1)
                    print(sel+'\n')
                    items = int(input("Please select one:"))
                
                       
        elif items == 5:
            print("Notebook shuttingdown, thank you.")
            break
 
                                      

if __name__ == "__main__":
    prog_one()

