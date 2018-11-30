#!/usr/bin/env python3
import os, sys

def convert(prompt):
    filename1 = "number.txt"
    filename2 = "notebook.txt"

    if prompt == filename1:
        return 1
    elif prompt == filename2:
        return 1
    else:
        return 0

def main():
    if convert(sample) == False:
        print("There seems to be no file with that name.")
        sys.exit(0)
        
    else:
        try:
            f = open(sample, "r")
            for i in f.readline().split('\ufeff'):
                if i.isnumeric():
                    int(i)
                    print("The result was",1000/int(i))
                    f.close()
                    sys.exit(0)
                
   
        except OSError:
            print("There seems to be no file with that name.")
        except ValueError:
            print("The file contents were unsuitable.")
            sys.exit(0)
        except Exception:
            print("There was a problem with the program.")
            
    while sample!= True:
        if convert(sample) == False:
            print("There seems to be no file with that name.")
            sys.exit(0)
            
        else:
            try:
                
                f = open(sample, "r")
            
                d = [(i) for i in f.readline()]
                print("The result was {}".format(1000/int(i)))
                sys.exit(0)
        
            except OSError:
                print("There seems to be no file with that name.")
                sys.exit(0)
            except ValueError:
                print("The file contents were unsuitable.")
                sys.exit(0)
            except Exception: 
                print("There was a problem with the program.")
                sys.exit(0)
        

if __name__ == "__main__":
    sample = input("Give the file name:")
    main()
         
