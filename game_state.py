from player import *
import random as rand
from session import *
import sys

"""
Holds game map + object state and update code (put code you want done each tick here) 
"""
weapons = [0,0,0,0,0]

class GameState:
    def __init__(self, doom_session):
        
        self.session = doom_session
        self.player = Player(doom_session)
        
        self.players = self.session.getPlayers()
        self.player.state = self.session.getPlayer()

        self.player.id = self.player.state.get("id",None)


    def poll(self):
        self.player.state = self.session.getPlayer()

        self.players =  [x for x in self.session.getPlayers() if x.get("id", None) != self.player.id]

    def update(self):
        if(self.players is not None):
            nearestPlayer = self.player.getNearestPlayer(self.players)
            print("Distance: ", self.player.getDistanceBtw(self.player,nearestPlayer))
            #print("players", self.players)
            
            self.player.update()
            self.player.move_to(nearestPlayer)

            if (self.player.inRange(nearestPlayer)):
                print ("inside if inRange")
                self.player.shootAt(player)
            
