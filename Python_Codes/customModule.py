#!/usr/bin/env python3

import sys, os

def testme(*args):
    for arg in args:
        if len(arg) < 5:
            print("The module says no.")
        elif arg.isalnum() is False:
            print("The module says no.")
        elif arg.isalpha() is True:
            print("The module says no.")
        elif arg.isdigit() is True:
            print("The module says no.")
        else:
            print("This string fits as password!")
            sys.exit(0)
    
    userinput = input("Give a string for testing: ")
    if len(userinput) < 5:
        print("The module says no.")
    elif userinput.isalnum() is False:
        print("The module says no.")
    elif userinput.isalpha() is True:
        print("The module says no.")
    elif userinput.isdigit() is True:
        print("The module says no.")
    else:
        print("This string fits for a password!")
        sys.exit(0)

    
    while True:
        userinput = input("Give a string for testing: ")
        if len(userinput) < 5:
            print("The module says no.")
        elif userinput.isalnum() is False:
            print("The module says no.")
        elif userinput.isalpha() is True:
            print("The module says no.")
        elif userinput.isdigit() is True:
            print("The module says no.")
        else:
            print("This string fits for a password!")
            sys.exit(0)
             
    testme(userinput)

if __name__ == "__main__":
    testme()
