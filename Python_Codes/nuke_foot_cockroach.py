#!/usr/bin/env python3

import sys
import random

def vector_one():

    rounds = 0
    d3 = 0
    c1 = 0
    c2 = 0
    counter = 20
    while True:
        rounds += 1
        ask_bio = input("Foot, Nuke or Cockroach? (Quit ends):")
        if ask_bio in ["Cockroach", "Nuke", "Foot"]:
            print("You chose:",ask_bio)
            ai = ["Cockroach", "Nuke", "Foot"]
            random.randint(1,3)
            e_robot = random.randint(1,3)
            if e_robot == 1:
                print("Computer chose:","Foot")
            elif e_robot == 2:
                print("Computer chose:","Nuke")
            else:
                print("Computer chose:","Cockroach")

            if ask_bio == "Nuke" and e_robot == 1:
                c1 += 1
                print ("You WIN!")
                
            elif ask_bio == "Nuke" and e_robot == 2:
                print("Both LOSE!")
                
            elif ask_bio  == "Foot" and e_robot == 2:
                print("You LOSE!")
            elif ask_bio == "Cockroach" and e_robot == 2:
                c1 += 1
                print ("You WIN!")
            elif ask_bio == "Nuke" and e_robot == 3:
                print("You LOSE!")
            elif ask_bio== "Foot" and e_robot == 3:
                c1 += 1
                print("You WIN!")
            elif ask_bio == "Cockroach" and e_robot == 1:
                print("You LOSE!")
            else:
                c2 += 1
                print("It is a tie!")

        elif ask_bio not in ["Cockroach", "Nuke", "Foot", "Quit"]:
            d3 += 1
            print("Incorrect selection.")
        elif ask_bio == "Quit":
            print("You played", (rounds-d3) - 1, "rounds, and won", c1, "rounds, playing tie in",c2, "rounds.")
            sys.exit()


if __name__ == "__main__":
    vector_one()
   