import argparse

class DoomSession:
    def __init__(self, ip, port):
        self.server_ip = ip
        self.server_port = port

    

        


class GameState:
    def __init__(self, doom_session):
        self.state = {}
        self.predicted_state = {}
        
        self.session = doom_session

    def poll(self):
        pass

    def update(self):
        pass

def main():
    parser = argparse.ArgumentParser(description="connects a player to a doom rest api session")
    parser.add_argument("-p" 


main()

