import os

from common.input_validation import get_input
from common.list_printer import print_list
from common.pickle_saving import *
from menu.main_menu import *
from menu.work.job import *


def play():
    saves = os.listdir()
    saves.append("Create New Save")
    print_list(saves)
    x = get_input(list, "Which save file do you want to load?", saves)
    if saves[x] == saves[-1]:
        main_menu(read_savefile(create_player().file_name))
    else:
        main_menu(read_savefile(saves[x]))

play()
# Job("Test", (0,10),0,(0,10),(0,10),0).do_job(5)
