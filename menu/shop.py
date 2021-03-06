from common.common_options import *
from common.value_validator import *
import menu.main_menu as menu
from PyInquirer import *

class Item:
    def __init__(self, name, cost, min_age, on_use_function=None):
        self.name = name
        self.cost = cost
        self.min_age = min_age
        self.on_use_function = on_use_function

pizza = Item("Pizza", 3, 0)
water = Item("Water", 3, 0)

item_dict = {
    f"{pizza.name} (${pizza.cost})": pizza,
    f"{water.name} (${water.cost})": water
}

def shop(player, items=list(item_dict.keys())):
    items = add_back(items)
    item_choices = [
        {
            "type": "list",
            "name": "item",
            "choices": [{"name": i} for i in items],
            "message": "What would you like to buy?"
        },
        {
            "type": "input",
            "name": "quantity",
            "message": "How many would you like to buy?",
            "validate": lambda answer: validate_amount(answer),
            "filter": lambda answer: int(answer),
        },
        {
            "type": "confirm",
            "name": "confirmation",
            "message": "Are you sure you want to purchase these items?",
            "default": True
        }
    ]
    item = prompt(item_choices[0])["item"]
    handle_special(item, player)
    amount = prompt(item_choices[1])["quantity"]
    ok = prompt(item_choices[2])["confirmation"]
    if ok:
        player.buy(item_dict[item],amount)
    remove_special(items, 1)
    return menu.main_menu(player=player)

