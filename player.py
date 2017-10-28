from session import *

"""
Holds session information and delegates requests (do ur api calls here)
"""
class Player:
    def __init__(self, doom_session):
        self.session = doom_session

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
   
