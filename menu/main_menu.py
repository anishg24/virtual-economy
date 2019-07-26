from __future__ import print_function, unicode_literals
from menu.work import work
from menu.stats import stats
from menu.shop import shop
from menu.bank import bank
from menu.inventory import inventory
from menu.settings import settings
from PyInquirer import *
from colorama import init
from termcolor import colored
init()

def main_menu(player):
    data = player.data
    name = data["name"]
    questions = [
        {
            "type": "list",
            "name": "action",
            "choices": [
                {
                    "name": "Next Month\n-- Money --"
                },
                {
                    "name": "Work"
                },
                {
                    "name": "Shop"
                },
                {
                    "name": "Bank\n-- Player --"
                },
                {
                    "name": "Inventory"
                },
                {
                    "name": "Stats\n-- Misc. --"
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
    if action == "next month":
        print(colored("Resting...","cyan"))
        player.next_month()
        main_menu(player)
    elif action == "quit":
        player.backup()
        print(colored("Thanks for playing! See you soon!","red"))
        quit()
    else:
        eval(f"{action}(player=player)")
