from common.input_validation import *
from common.list_printer import print_list
from menu.work import work
from menu.stats import stats
from menu.settings import settings
from PyInquirer import *


def main_menu(player, options=["work","shop","bank","settings","stats","quit"]):
    data = player.data
    name = data["name"]
    questions = [
        {
            "type": "list",
            "name": "action",
            "choices": [{"name": i.capitalize()} for i in options],
            "message": f"What would you like to do {name.capitalize()}?"
        }
    ]
    action = prompt(questions[0])["action"].lower()
    if action == "quit":
        player.backup()
        print("Thanks for playing! See you soon!")
        quit()
    else:
        eval(f"{action}(player=player)")
 
