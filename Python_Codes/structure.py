#!/usr/bin/env python3

name = "John"
password = "ABC123"


name = input("Give name:")

if name == "John":
	password = input("Give password:")
	if password == "ABC123":
		print("Both inputs are correct!")
								 
		
	else:
		print("The password is incorrect.")
	
   
else:
    print("The given name is wrong.")
	