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
        print(self.player.state)
        self.objectsInfo = self.session.getObjects()
        self.player.id = self.player.state.get("id",None)


    def poll(self):
        self.player.state = self.session.getPlayer()
        self.player.update()
        self.players =  [x for x in self.session.getPlayers() if x.get("id", None) != self.player.id]
        self.objects = self.session.getObjects()

    def getShotguns(self):
        shotguns = list()
        for thing in self.objectsInfo:
            if thing["type"] == "Shotgun":
                shotguns.append(thing)
        return shotguns

    def getNearestShotgun(self, shotguns):
        min = 100000
        i= 0
        nearest = shotguns[0]
        for shotgun in shotguns:
            distance = self.player.getDistanceBtwShotgun(self.player,shotgun)
            if  distance < min:
                min = distance
                nearest = shotguns[i]
            i = i + 1
        return nearest

    def update(self, noShotgun):
        """
        if(self.state.player["health"] == 0):
            pressSpace()
        """
        print ("our weapon index: ", self.player.state.get("weapon"))
        if(self.player.state.get("weapon") == 2):
            noShotgun = False
        if(noShotgun):
            nearestShotgun = self.getNearestShotgun(self.getShotguns())
            self.player.move_to(nearestShotgun)

        if((self.players is not None) and (not noShotgun)): #and rand.randint(0, 10)==0
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
