from session import *
import math as maths

"""
Holds session information and delegates requests (do ur api calls here)
"""
class Player:
    def __init__(self, doom_session):
        self.session = doom_session
        self.forwards = True
        self.turning =  False



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

    def turn_to(self, x_move, y_move):
        x,y,_ = self.state.get("position", {}).values()

        #print(f"X: {x_move}, Y: {y_move}\n\n")
        angle = maths.degrees(maths.atan2(y_move-y , x_move-x)) 
        angle = angle if angle >= 0 else angle + 360

        player_angle = self.state.get("angle", 0)
        turn_angle = (player_angle-angle)
        
        if (not self.turning):
            self.turn(maths.copysign(5, turn_angle))
            self.turning = True


    def move_to(self, x,y):
        self.turn_to(x,y)
        self.forwards = True

    def move_to_player(self, other):
        self.move_to(*list(other.get("position").values())[:2] )

    def update(self):
        if (self.forwards):
            self.move_y(12)
        if (self.turning):
            self.turning = False


   
