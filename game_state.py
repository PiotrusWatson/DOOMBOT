from player import *
import random as rand
from session import *
import sys

"""
Holds game map + object state and update code (put code you want done each tick here) 
"""

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
		self.player.move_to_player(self.players[0])
		self.player.update()

		if (rand.randint(0,4*15) == 0):
			#self.player.turn_to_player(self.players[0])
			self.player.shoot()
			
