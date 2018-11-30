#!/usr/bin/env python3
import sys,os
from math import sin, cos
a= ("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
    "(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")

print("Calculator")
while True:
    try:
        s = int(input("Give a number:"))
        if type(s) != int:
            s = int(input("Give a number:"))
            raise Exception
        else:
            break  
    except Exception:
        print("This input is invalid.")
        
while True:
    try:
        t = int(input("Give a number:"))
        if type(t) == int:
            print(a)
            print("Current numbers:" ,s,t)
            break
        else:
            t = int(input("Give a number:"))
            raise Exception
    except Exception:
        print("This input is invalid.")
                

karma = True   

while karma:
    eventhorizon = int(input("Please select something (1-6):"))
    if eventhorizon == 1:
        print("The result is:",s + t)
        print(a)
        print("Current numbers:" ,s,t)
    elif eventhorizon == 2:
        print("The result is:",s - t)
        print(a)
        print("Current numbers:" ,s,t)
        
    elif eventhorizon == 3:
        print("The result is:",s * t)
        print(a)
        print("Current numbers:" ,s,t)
    elif eventhorizon == 4:
        print("The result is:",s / t)
        print(a)
        print("Current numbers:" ,s,t)
    elif eventhorizon == 5:
        print("The result is:",(sin(s / t)))
        print(a)
        print("Current numbers:" ,s,t)
    elif eventhorizon == 6:
        print("The result is:",(cos(s / t)))
        print(a)
        print("Current numbers:" ,s,t)
        
    elif eventhorizon == 7:
        while True:
            try:
                s = int(input("Give a number:"))
                if type(s) != int:
                    s = int(input("Give a number:"))
                    raise Exception
                else:
                    break
            except Exception:
                print("This input is invalid.")
        while True:
            try:
                t = int(input("Give a number:"))
                if type(t) == int:
                    print(a)
                    print("Current numbers:" ,s,t)
                    break
                else:
                    t = int(input("Give a number:"))
                    raise Exception
            except Exception:
                print("This input is invalid.")
                
    elif eventhorizon == 8:
        print("Thank you!")
        sys.exit(0)
           
