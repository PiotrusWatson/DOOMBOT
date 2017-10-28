import argparse
import requests
import random as rand
import time

"""
Holds session information and delegates requests (do ur api calls here)
"""
class DoomSession:

    def __init__(self, ip, port):
        self.server_ip = ip
        self.server_port = port
        self.url = "http://{}:{}/api/".format(ip, port)

    def sendAction(self, action):
        try:
            requests.post(self.url+"player/actions", json=action)
            print(action)
        except:
            print("Send Action POST FAILED")

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
            
 
    
def main():
    #parser = argparse.ArgumentParser(description="connects a player to a doom rest api session")
    #parser.add_argument("-p")
    sesh = DoomSession("localhost", "6001")
    state = GameState(sesh)
    
    while(True):
        state.poll()
        state.update()
        time.sleep(1/30)

    


main()

