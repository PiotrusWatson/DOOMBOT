from session import *
import math

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
        
        turn_angle = self.getangle(x, y, x_move, y_move)

        print("turn angle: " + str(turn_angle) +"\n")
        if (not self.turning):
            self.turn(turn_angle)
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

    def getangle(self, x, y, x_move, y_move):
        #print("X:" + str(x_move) + "Y: " + str(y_move), "\n\n")
        angle = math.degrees(math.atan2(y_move-y , x_move-x)) 
        angle = angle if angle >= 0 else angle + 360


        player_angle = self.state.get("angle", 0)
        turn_angle = (player_angle-angle)

        if abs(turn_angle) > 180:
            if turn_angle > 0:
                turn_angle = turn_angle - 360
            else:
                turn_angle = turn_angle + 360


        
        return turn_angle

    def getDistanceBtw(self, object1, object2):
        z1,x1,y1 = object1.state.get("position", {}).values()
        z2,x2,y2 = object2.get("position", {}).values()
        return self.getDistance(x1, y1, x2, y2)


    def getDistance(self, x1, y1, x2, y2):
        x_diff = x2 - x1
        x_diff_squared = x_diff * x_diff
        y_diff = y2 - y1
        y_diff_squared = y_diff * y_diff
        distance = math.sqrt(x_diff_squared + y_diff_squared)
        return distance

        

   
