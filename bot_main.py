import argparse
import requests
import random as rand
import time

from session import *
from player import *
from game_state import *

"""
Initialises session and handles arg passing, maybe later can do things involving doom client + server
"""

    
def main():
    #parser = argparse.ArgumentParser(description="connects a player to a doom rest api session")
    #parser.add_argument("-p")
    sesh = DoomSession("localhost", "6001")
    state = GameState(sesh)
    
    while(True):
        state.poll()
        state.update()
        time.sleep(1/5)

    


main()

