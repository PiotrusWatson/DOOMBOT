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

    def turn(self, angle):
        if (angle < 0):
            action_type = "turn-left"
        else:
            action_type = "turn-right"
            
        self.session.sendAction({"type": action_type, "amount": abs(angle)})
#todo: make nicer using factories (maybe dicts of dicts?)
        
    def shoot(self):
        self.session.sendAction({"type": "shoot"})
    
    def move_y(self, amount):
        if (amount < 0):
            action_type = "backward"
        else:
            action_type = "forward"

        self.session.sendAction({"type": action_type, "amount": abs(amount)})

    def move_x(self, amount):
        if (amount < 0):
            action_type = "strafe-left"
        else:
            action_type = "strafe-right"

        self.session.sendAction({"type": action_type, "amount": abs(amount)})

    """
    turns towards a specific point 
    """
    def turn_to(self, x_move, y_move):
        
        x,y,_ = self.state.get("position", {}).values()

        angle = maths.degrees(maths.atan2(y_move-y , x_move-x)) 
        angle = angle if angle >= 0 else angle + 360

        
        player_angle = self.state.get("angle", 0)
        turn_angle = (player_angle-angle)
        
        self.turn(maths.copysign(self.rotateSpeed, turn_angle))

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
	game_state THIS IS BAD TODO: NOT HAVE IT DO THAT
	"""
    def update(self):
        if (self.forwards):
            self.move_y(self.forwardSpeed)
    
    def updateState(self, state):
        self.state = state
