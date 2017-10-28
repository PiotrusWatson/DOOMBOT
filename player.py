from session import *
import math as maths

"""
Holds session information and delegates requests (do ur api calls here)
"""
class Player:
	def __init__(self, doom_session):
		self.session = doom_session
		self.forwards = True
		self.forwardSpeed = 12
		self.rotateSpeed = 5 #set too high and we infinite loop
		self.state = {} #stores EVERYTHING about player (from API)

	'''
	Takes angle and decides whether player is turning left or right
	'''
	def turn(self, angle):
		if (angle < 0):
			action_type = "turn-left"
		else:
			action_type = "turn-right"
			#sends angle to api to turn player
		self.session.sendAction({"type": action_type, "amount": abs(angle)})
#todo: make nicer using factories (maybe dicts of dicts?)
		
	def shoot(self):
		self.session.sendAction({"type": "shoot"})
	
	"""
	Sets action type for y-axis movement then sends it to the api
	"""
	def move_y(self, amount):
		if (amount < 0):
			action_type = "backward"
		else:
			action_type = "forward"

		self.session.sendAction({"type": action_type, "amount": abs(amount)})

	"""
	Sets action type for y-axis movement then sends it to api
	"""
	def move_x(self, amount):
		if (amount < 0):
			action_type = "strafe-left"
		else:
			action_type = "strafe-right"
	#strafes depending on action type
		self.session.sendAction({"type": action_type, "amount": abs(amount)})

	"""
	turns towards a specific point 
	"""
	def turn_to(self, x_move, y_move):
		
		x,y,_ = self.state.get("position", {}).values()

	#get angle between player and thing
		angle = maths.degrees(maths.atan2(y_move-y , x_move-x)) 
		if x_move < x:
			angle = angle + 180
		if angle < 0:
			angle = angle + 360
	
		print ("angle between player and object: " + str(angle))
		player_angle = self.state.get("angle", 0)
		print ("player angle: " + str(player_angle))
		turn_angle = -(player_angle-angle)
		print ("turn_angle: " + str(turn_angle))
		
		self.turn(turn_angle) #rotateSpeed?

	"""
	turns to a specific point _ moves TODO RENAME + MAKE PROPER STRAFES
	"""
	def move_to(self, x,y):
		self.turn_to(x,y)
		self.forwards = True

	"""
	GETS ANOTHER PLAYER FROM ??? + TURNS/MOVES
	"""
	def move_to_player(self, other):
		self.move_to(*list(other.get("position").values())[:2] )

	"""
	eventually we'll put all the movement logic in here? right now it's spread between here and 
	game_state THIS IS BAD TODO: NOT HAVE IT DO THAT0
	"""
	def update(self):
		if (self.forwards):
			self.move_y(self.forwardSpeed)
	
	def updateState(self, state):
		self.state = state


	
