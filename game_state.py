from player import *
import random as rand
from session import *

"""
Holds game map + object state and update code (put code you want done each tick here) 
"""

class GameState:
    def __init__(self, doom_session):
        self.state = {}
        self.predicted_state = {}
        
        self.session = doom_session
        self.player = Player(doom_session)

    def poll(self):
        pass

    def update(self):
        self.player.turn(5)
        if (rand.randint(0,4*15) == 0):
            self.player.shoot()
            
