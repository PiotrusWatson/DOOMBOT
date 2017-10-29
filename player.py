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

        action_type = "turn-right"
        self.session.sendAction({"type": action_type, "amount": abs(angle)})

    def fastTurn(self, angle):
        if (angle < 0):
            angtype = "left"
        else:
            angtype = "right"
        self.session.sendTurn({"type": angtype, "target_angle": angle})
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
        x = self.state.get("position", {})["x"]
        y = self.state.get("position", {})["y"]
        x_thing = thing.get("position")["x"]
        y_thing = thing.get("position")["y"]
        angle_to_face = self.getAngleToFace(x, y, x_thing, y_thing)
        print ("angle facing: ", self.state.get("angle", 0))
        print("angle to face: " + str(angle_to_face) +"\n")
        if (not self.turning):
            self.fastTurn(angle_to_face)
            self.turning = True


    def move_to(self, other):
        self.turn_to(other)
        self.forwards = True

    def update(self):
        if (self.forwards):
            self.move_y(12)
        if (self.turning):
            self.turning = False

    def getAngleToFace(self, x, y, x_move, y_move):
        #print("X:" + str(x_move) + "Y: " + str(y_move), "\n\n")
        alpha = math.degrees(math.atan2(abs(y_move-y) , abs(x_move-x)))
        if (y_move > y and x_move > x):
            angle_to_face = alpha
        if (y_move > y and x_move < x):
            angle_to_face = 180 - alpha
        if (y_move < y and x_move > x):
            angle_to_face = 360 - alpha
        if (y_move < y and x_move < x):
            angle_to_face = 180 + alpha
        if (y_move == y and x_move > x):
            angle_to_face = 0
        if (y_move == y and x_move < x):
            angle_to_face = 180
        if (y_move > y and x_move == x):
            angle_to_face = 90
        if (y_move < y and x_move == x):
            angle_to_face = 270
        return angle_to_face
        """
        #player_angle = self.state.get("angle", 0)
        if (abs(angle) < 30):
            turn_angle = 0
        else:
            turn_angle = 0.9
        #turn_angle = math.copysign(0.5, turn_angle)
        print("Turn Angle", angle)
        """


    def getDistanceBtwShotgun(self, object1, object2):
        x1 = object1.state.get("position")["x"]
        y1 = object1.state.get("position")["x"]
        x2 = object2.get("position")["x"]
        y2 = object2.get("position")["y"]
        """
        z1,x1,y1 = object1.state.get("position", {}).values()
        z2,x2,y2 = object2.get("position", {}).values()
        """
        return self.getDistance(x1, y1, x2, y2)

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
        print("Our weapon index: ", weaponIndex)
        ourRange = ranges[weaponIndex]
        print("Our range is: ", ourRange)
        print("Ditance in this function is: ", self.getDistanceBtw(self, player))
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
