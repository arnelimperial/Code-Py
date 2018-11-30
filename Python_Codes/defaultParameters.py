#!/usr/bin/env python3
import sys
def tester(givenstring = 'Too short'):

    if givenstring == 'quit':
        sys.exit()
        return
    
    else:
        pass
    
    second = len(givenstring)
    
    if second < 10:
        print('Too short')
        
    else:
        print(givenstring)
        
    
import sys
        
def main():
    while True:
        line = input("Write something (quit ends):")
        tester(line)


        
            
if __name__ == "__main__":
    main()


