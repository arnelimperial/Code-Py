#!/usr/bin/env python3

print("Calculator")

denatured = int(input("Give the first number:"))
cleaved = int(input("Give the second number:"))

print("(1) +\n(2) -\n(3) *\n(4) /")

coagulate = int(input("Please select something (1 - 4):"))

if coagulate == 1:
    print ("The result is:", denatured + cleaved)
elif coagulate == 2:
    print("The result is:", denatured - cleaved)
elif coagulate == 3:
    print("The result is:", denatured * cleaved)
elif coagulate == 4:
    print("The result is:", denatured / cleaved)

elif coagulate <= 5:
    print("Selection was not correct.")

else:
    print("Selection was not correct.")

