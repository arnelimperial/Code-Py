#!/usr/bin/env python3

from math import sin, cos
print("Calculator")
s = int(input("Give the first number:"))
t = int(input("Give the second number:"))
a= ("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
    "(5)sin(number1/number2)\n(6)cos(number1/number2)\n(7)Change numbers\n(8)Quit")
print(a)

print("Current numbers:" ,s,t)


summer = True   

while summer:
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
        s = int(input("Give the first number:"))
        t = int(input("Give the second number:"))
        print(a)
        print("Current numbers:" ,s,t)
    elif eventhorizon == 8:
        print("Thank you!")
        break
           
    