#!/usr/bin/env python3

import sys, os

def printme(*args):
        for arg in args:
                print("I got:", arg)
        for arg in args:
            print("The parameter was",len(arg),"characters long.")


string_sample= "Exampleline"

        
if __name__ == "__main__":
   printme(string_sample)

