from __future__ import print_function, unicode_literals
from common.input_validation import *
from common.list_printer import print_list
from menu.work import work
from menu.stats import stats
from menu.shop import shop
from menu.inventory import inventory
from menu.settings import settings
from PyInquirer import *


def main_menu(player):
    data = player.data
    name = data["name"]
    questions = [
        {
            "type": "list",
            "name": "action",
            "choices": [
                {
                    "name": "Next Day\n-=- Money -=-"
                },
                {
                    "name": "Work"
                },
                {
                    "name": "Shop"
                },
                {
                    "name": "Bank\n-=- Player -=-"
                },
                {
                    "name": "Inventory"
                },
                {
                    "name": "Stats\n-=- Misc. -=-"
                },
                {
                    "name": "Settings"
                },
                {
                    "name": "Quit"
                }
            ],
            "message": f"What would you like to do {name.capitalize()}?"
        }
    ]
    action = prompt(questions[0])["action"].lower().split("\n")[0]
    if action == "next day":
        print("Resting...")
        player.next_day()
        main_menu(player)
    elif action == "quit":
        player.backup()
        print("Thanks for playing! See you soon!")
        quit()
    else:
        eval(f"{action}(player=player)")
 
