import requests
import json


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
        except Exception as e:
            print(e)

    def sendTurn(self, action):
        try:
            x = requests.post(self.url+"player/turn", json=action)
            #print(x.content)
        except Exception as e:
            print(e)
    def getPlayers(self):
        try:
            result = requests.get(self.url+"players")
            #print(result.text)
        except:
            print("GET PLAYERS REQUEST FAILED")
        return json.loads(result.text)

    def getPlayer(self):
        try:
            result = requests.get(self.url+"player")
        except:
            print("GET PLAYERS REQUEST FAILED")
        return json.loads(result.text)

    def getObjects(self):
        try:
            result = requests.get(self.url+"world/objects")
        except Exception as e:
            print(e)

        return json.loads(result.text)
