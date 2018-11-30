#!/usr/bin/env python3
def poweroftwo(num):
    square = 2 ** num
    print("The result is", square)
    
    
def main():

    number = int(input("Give a number:"))
    number = poweroftwo(number)



if __name__ == "__main__":
    main()
