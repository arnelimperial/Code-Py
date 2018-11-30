#!/usr/bin/env python3

class Player:
    team = "Blue"
    points = 1

    def tellscore(self):
        print("I am", self.team, ",we have", self.points, "points!")
    
play = Player()
play.tellscore()
   
