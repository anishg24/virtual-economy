from PyInquirer import *
import menu.main_menu as menu

back_val = "⇠ Back"
quit_val = "⨯ Quit"

def add_back(data):
    data.append(back_val)
    return data

def add_quit(data):
    data.append(quit_val)
    return data

def add_special(data):
    data = add_back(data)
    data = add_quit(data)
    return data

def handle_special(choice, player):
    if choice == back_val:
        return menu.main_menu(player=player)
    elif choice == quit_val:
        player.backup()
        print("Thanks for playing! See you soon!")
        return quit()

def remove_special(data, amount):
    for _ in range(0,amount):
        del data[-1]
    return data
