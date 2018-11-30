#!/usr/bin/env python3
import sys
def tester(givenstring = 'Too short'):
    
    if givenstring == 'quit':
        sys.exit()
        return
    
    else:
        pass
         

        
def main():
    while True:
        line = input("Write something (quit ends):")
        tester(line)
        w = lambda x: "Too short" if len(x) < 10 else x 
        print(w(line))
        z = lambda x: "X spotted!" if x.find('X')!=-1 else""
        print(z(line))
   
            
if __name__ == "__main__":
    main()

