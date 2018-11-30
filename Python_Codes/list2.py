#!/usr/bin/env python3
import sys, os
x = [1,3]
while x:
    sel = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?:"))
    if sel == 1:
        item = input("What will be added?:")
        a = []
        a.append(item)
        sel1 = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?:"))
        
        if sel1 == 1:
            item1 = input("What will be added?:")
            a.append(item1)
            sel2 = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?:"))
            
            if sel2 == 1:
                item2 = input("What will be added?:")
                a.append(item2)
           
            elif sel2 == 2:
                print("There are",len(a),"items in the list.")
                sel_del = int(input("Which item is deleted?:"))
                try:
                    a.pop(sel_del)
                except IndexError:
                    print('Incorrect selection.')
            elif sel1 == 3:
                print("The following items remain in the list:")
                print(",".join(a))
                sys.exit(0)
            else:
                print("Incorrect selection.")
                 
            
        elif sel1 == 2:
            print("There are",len(a),"items in the list.")
            sel_del = int(input("Which item is deleted?:"))
            try:
                a.pop(sel_del)
                sel2 = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?:"))
                
                if sel2 == 1:
                    item2 = input("What will be added?:")
                    a = []
                    a.append(item1)
                elif sel2 == 2:
                    print("There are",len(a),"items in the list.")
                    sel_del = int(input("Which item is deleted?:"))
                    try:
                        a.pop(sel_del)
                    except IndexError:
                        print('Incorrect selection.')
                elif sel1 == 3:
                    print("The following items remain in the list:")
                    print(",".join(a))
                    sys.exit(0)
                else:
                    print("Incorrect selection.")
                 

            except IndexError:
                print('Incorrect selection.')
                sel1 = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?:"))
               
                if sel1 == 1:
                    item1 = input("What will be added?:")
                    a = []
                    a.append(item1)
                elif sel1 == 2:
                    print("There are",len(a),"items in the list.")
                    sel_del = int(input("Which item is deleted?:"))
                    try:
                        a.pop(sel_del)
                    except IndexError:
                        print('Incorrect selection.')
                elif sel1 == 3:
                    print("The following items remain in the list:")
                    print(",".join(a))
                    sys.exit(0)
                else:
                    print("Incorrect selection.")
            
                
        elif sel1 == 3:
            print("The following items remain in the list:")
            print(",".join(a))
            sys.exit(0)
        else:
            print("Incorrect selection.")
                    
    
    elif sel == 2:
        print("There are",len(a),"items in the list.")
        sel_del = int(input("Which item is deleted?:"))
        try:
            a.pop(sel_del)
          
        except IndexError:
            print('Incorrect selection.')
            sel = int(input("Would you like to\n(1)Add or\n(2)Remove items or\n(3)Quit?:"))
            if sel == 1:
                item = input("What will be added?:")
                a = []
                a.append(item)
            elif sel == 2:
                print("There are",len(a),"items in the list.")
                sel_del = int(input("Which item is deleted?:"))
                try:
                    a.pop(sel_del)
                except IndexError:
                    print('Incorrect selection.')
                       
            elif sel == 3:
                print("The following items remain in the list:")
                print(",".join(a))
                sys.exit(0)

            else:
                print("Incorrect selection.")
                 
    
    elif sel == 3:
        print("The following items remain in the list:")
        print(",".join(a))
        sys.exit(0)

    else:
        print("Incorrect selection.")
        
