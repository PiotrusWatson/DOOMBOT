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
        self.player.update()
        self.players =  [x for x in self.session.getPlayers() if x.get("id", None) != self.player.id]
        self.objects = self.session.getObjects()

    def update(self):
        if((self.players is not None) ): #and rand.randint(0, 10)==0
            nearestPlayer = self.player.getNearestPlayer(self.players)
            print("Distance: ", self.player.getDistanceBtw(self.player,nearestPlayer))
            #print("players", self.players)


            self.player.move_to(nearestPlayer)
            if(self.player.getDistanceBtw(self.player,nearestPlayer) < 1500):
                self.player.shootAt(nearestPlayer)
            """
            if (self.player.inRange(nearestPlayer)):
                print ("inside if inRange")
                self.player.shootAt(nearestPlayer)
            """

        def getObjectsByType(self, type):
            objcollection = []
            for obj in self.objects:
                if (obj["type"] == type):
                    objcollection.append(self.object.index(obj))

            return objcollection
