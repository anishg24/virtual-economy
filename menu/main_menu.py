from common.input_validation import *
from common.list_printer import print_list
from menu.work import work

def main_menu(player, options=["work","shop","settings","stats","quit"]):
    data = player.data
    name = data["name"]
    print("\n----------------------------------------------------")
    print_list(options, end="  ")
    print("\n----------------------------------------------------")
    action = get_input(list, f"\nWhat would you like to do {name.capitalize()}?", options)
    if options[action] == "stats":
        print("Money: $" + str(data["money"]))
        print("Bank Amount: $" + str(data["bank"]))
        print("Experience: " + str(data["xp"]) + " XP")
        main_menu(player=player)
    elif options[action] == "quit":
        player.quit_sequence()
    else:
        eval(f"{options[action]}(player=player)")
 
