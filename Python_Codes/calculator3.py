#!/usr/bin/env python3
print("Calculator")
s = int(input("Give the first number:"))
t = int(input("Give the second number:"))
print("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
      "(5) Change numbers\n(6) Quit")
print("Current numbers:" ,s,t)

summer = True   

while summer:
    eventhorizon = int(input("Please select something (1-6):"))
    if eventhorizon == 1:
        print("The result is:",s + t)
        print("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
              "(5) Change numbers\n(6) Quit")
        print("Current numbers:" ,s,t)
    elif eventhorizon == 2:
        print("The result is:",s - t)
        print("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
              "(5) Change numbers\n(6) Quit")
        print("Current numbers:" ,s,t)  
    elif eventhorizon == 3:
        print("The result is:",s * t)
        print("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
              "(5) Change numbers\n(6) Quit")
        print("Current numbers:" ,s,t)
    elif eventhorizon == 4:
        print("The result is:",s / t)
        print("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
              "(5) Change numbers\n(6) Quit")
        print("Current numbers:" ,s,t)
    elif eventhorizon == 5:
        s = int(input("Give the first number:"))
        t = int(input("Give the second number:"))
        print("\n\n(1) +\n(2) -\n(3) *\n(4) /\n"
              "(5) Change numbers\n(6) Quit")
        print("Current numbers:" ,s,t)
    elif eventhorizon == 6:
        print("Thank you!")
        break
           