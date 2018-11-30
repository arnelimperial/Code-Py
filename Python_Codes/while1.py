#!/usr/bin/env python3

# -*- coding: cp1252 -*-

# Two variables used to determine how many laps
#will the program turns to print "This lap is" starting to 0 rounds.

rounds = 0
turn = 5

#The iteration terminates if the value of rounds > turn.
while rounds < turn:
    print("This is lap", rounds)
    #Increment round value by 1 in each turn.
    rounds = rounds + 1
