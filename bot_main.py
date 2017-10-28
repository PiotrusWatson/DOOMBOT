import argparse
import requests


class DoomSession:
    def __init__(self, ip, port):
        self.server_ip = ip
        self.server_port = port
		self.url = "http://{}:{}/api/".format(ip, port)

	def sendAction(action):
		url"actions"

        


class GameState:
    def __init__(self, doom_session):
        self.state = {}
        self.predicted_state = {}
        
        self.session = doom_session

    def poll(self):
        pass

    def update(self):
        


class Player:
	def __init__(self, doom_session):
		self.session = doom_session

	def turn(angle):
		if (angle < 0):
			action_type = "turn-left"
		else:
			action_type = "turn-right"
		self.session.sendAction({"type": action_type, "amount": abs(angle)}
#todo: make nicer using factories (maybe dicts of dicts?)
	def shoot():
		self.session.sendAction({"type": "shoot"})
	
	def move_y(amount):
		if (amount < 0):
			action_type = "backward"
		else:
			action_type = "forward"

		self.session.sendAction({"type": action_type, "amount": abs(amount)})

	def move_x(amount):
		if (amount < 0):
			action_type = "strafe-left"
		else:
			action_type = "strafe-right"

		self.session.sendAction({"type": action_type, "amount": abs(amount)})
	
	
def main():
    parser = argparse.ArgumentParser(description="connects a player to a doom rest api session")
    parser.add_argument("-p")


main()

