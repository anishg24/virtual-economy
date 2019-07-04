from PyInquirer import *
import menu.main_menu as menu
from prettytable import PrettyTable


def inventory(player):
    inventory = player.data["inventory"]
    pt = PrettyTable()
    if bool(inventory):
        pt.field_names = ["Item", "Count"]
        for i in inventory:
            pt.add_row([i, inventory[i][0]])
    else:
        pt.field_names = ["Your inventory is empty!"]
    print(pt)
    menu.main_menu(player=player)
