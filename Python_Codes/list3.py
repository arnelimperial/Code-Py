#!/usr/bin/env python3

import sys,os
os.getcwd()
with open('words.txt', 'r') as f:
    x = f.readlines()
    l = [s.replace('\n', '') for s in x]
    k = [s.strip('\ufeff') for s in l]
    q = sorted(k)
    h = '\n'.join(q)
    print("Words in an alphabetical order:")
    print(h)

    

