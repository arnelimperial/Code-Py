#!/usr/bin/env python3
xuq = int(input("Give a number:"))
zuq = int(input("Give another number:"))

if (xuq%2 == 0) and (zuq%2 == 1):
	print("One of the numbers is even.")
	
elif (xuq%2 == 0) or (zuq%2 == 0):
	print("Both numbers are even.")
	
else:
	print("Both numbers are odd.")


	
		  