#!/usr/bin/env python3

class Player:
    team = "Blue"
    points = "300"

    def var(self):
        print("The", self.team, "contender has", self.points, "points!")
    
play = Player()
play.var()

