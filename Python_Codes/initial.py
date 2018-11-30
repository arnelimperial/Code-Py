#!/usr/bin/env python3

import os, sys

class Player:
   
    def __init__(self):
        self.player1 = "Blue"
        self.player2 = "Red"
        self.player3 = "Black"
        self.player4 = "White"
        self.point1 = "2"
        self.point2 = "1"
        
    def goal(self):
        print("I am", self.player1, ",we have",self.point1, "points!")
        print("I am", self.player2, ",we have",self.point2, "points!")
    def tellscore(self):
        print("I am", self.player3, ",we have",self.point1, "points!")
        print("I am", self.player4, ",we have",self.point2, "points!")
        
        
def main():
    on = Player()
    
    prompt = input("What color do I get?:")
    prompt1 = input("What color do I get?:")

    if prompt == "Blue" and prompt1 == "Red":
        on.goal()
    elif prompt == "Black" and prompt1 == "White":
        on.tellscore()

        
            
    
if __name__ == "__main__":
    main()

