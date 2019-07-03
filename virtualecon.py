#  _    ___      __              __
# | |  / (_)____/ /___  ______ _/ /
# | | / / / ___/ __/ / / / __ `/ / 
# | |/ / / /  / /_/ /_/ / /_/ / /  
# |___/_/_/   \__/\__,_/\__,_/_/   
#                                 
#     ______                                      
#    / ____/________  ____  ____  ____ ___  __  __
#   / __/ / ___/ __ \/ __ \/ __ \/ __ `__ \/ / / /
#  / /___/ /__/ /_/ / / / / /_/ / / / / / / /_/ / 
# /_____/\___/\____/_/ /_/\____/_/ /_/ /_/\__, /  
#                                        /____/   
#
# Description: Command line game designed to mimic an aspect of life. You can work and buy things, simply by using arrow keys
#              and such. Try to reach as high as possible. You can also use your file and share with your friends (located in ./saves/)
# Author: Anish Govind
# Version: 0.0.5 (Beta)
# Dependencies: PyInquirer, PyFiglet, PrettyTable, Random, Pickle
# GitHub: https://github.com/generaldefence
#
# TO-DO:
#   - Finish shop options
#   - Finish main menu
# IDEAS:
#   - Stocks
#   - Limit to # of jobs worked in 1 day


import os

from common.input_validation import get_input
from common.list_printer import print_list
from common.player import *
from menu.main_menu import *
from menu.job import *
from pyfiglet import Figlet

f = Figlet(font='slant')
print(f.renderText('Virtual Economy'))


def play():
    saves = os.listdir()
    saves.append("Create a new save")
    saves.append("Quit")
    questions = [
        {
            "type": "list",
            "name": "save_num",
            "message": "Which save file do you want to load?",
            "choices": [{"name": i.capitalize()} for i in saves]
        }
    ]
    x = prompt(questions)["save_num"]
    if x == saves[-2]:
        main_menu(create_player())
    elif x == saves[-1]:
        print("Thanks for playing!")
        quit()
    else:
        main_menu(read_savefile(x))

play()

