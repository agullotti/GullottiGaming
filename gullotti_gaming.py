# Return to
# A text based RPG from Gullotti Gaming
# 6/16/2019
# Andy J Gullotti

# imports
import cmd
import textwrap
import sys
import os
import time
import random

#variables
screen_width = 100

# Create player class
class player:
    def __init__(self):
        self.name =''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
myPlayer = player()


#### Title Screen ###
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("controls"):
        controls_menu()
    elif option.lower == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'controls', 'quit']:
        print("please select from one of the available options")
        option = input("> ")
        if option.lower == ("play"):
            start_game()
        elif option.lower == ("controls"):
            controls_menu()
        elif option.lower == ("exit" or "exit game"):
            sys.exit()


def title_screen():
    os.system('clear')
    print('##########################')
    print('#   Welcome to ________  #')
    print('##########################')
    print('#       - Play           #')
    print('#       - Controls       #')
    print('#       - Exit Game      #')
    print('##########################')

def controls_menu():
    print('Move with W,A,S,D')
    print('Look by typing "Look"')
    print('exit Controls by typing "back"')
    controls_menu_option = ''
    while controls_menu_option != 'back':
        controls_menu_option = input('Please Type "back" to go back to Main Menu')
        break

title_screen()
title_screen_selections()