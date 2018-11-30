#!/usr/bin/env python3
# -*- coding: cp1252 -*-

#True value is assign to variable Proceed to introduce infinite loop.
Proceed = True

#Iteration of variable proceed with encoder as input variable.

while Proceed:
    encoder = input("Write something:")
	
	#If encoder inputs Quits which is False
	#value the loop will stop and prints "Bye bye!"
    if encoder =="quit":
        Proceed = False
        print("Bye bye!")

    else:
        print(encoder)