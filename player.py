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

    def turn_to(self, thing):
        x,y,_ = self.state.get("position", {}).values()
        x_thing = thing.get("position")["x"]
        y_thing = thing.get("position")["y"]
        turn_angle = self.getangle(x, y, x_thing, y_thing)

        print("turn angle: " + str(turn_angle) +"\n")
        if (not self.turning):
            self.turn(turn_angle)
            self.turning = True


    def move_to(self, other):
        self.turn_to(other)
        self.forwards = True

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

        
    def inRange(self, player):
        ranges = [50,50,1500,1500,0,0,0,0]
        weaponIndex = self.state.get("weapon")
        ourRange = ranges[weaponIndex]
        return (ourRange >= self.getDistanceBtw(self, player))

    def shootAt(self, player):
        self.turn_to(player)
        self.shoot()

    def getNearestPlayer(self, players):
        min = 100000
        i= 0
        for otherPlayer in players:
            distance = self.getDistanceBtw(self,otherPlayer)
            if  distance < min:
                min = distance
                nearest = players[i]
            i = i + 1
        return nearest
   
