from random import random, randrange
import menu.main_menu as menu
from colorama import init
from common.common_options import *
from common.value_validator import *
from prettytable import PrettyTable
from PyInquirer import *
from termcolor import colored

init()


class Bank:
    def __init__(self, name, interest_rate, initial_deposit, minimum_deposit, min_xp):
        self.name = name
        if 0 < interest_rate <= 100:
            self.interest_rate = interest_rate
        else:
            return
        self.initial_deposit = initial_deposit
        self.minimum_deposit = minimum_deposit
        self.min_xp = min_xp


sketchex = Bank("Sketchex", 2, 10, 5, 0)
better_bank = Bank("Better Bank", 3, 10, 5, 0)

bank_dict = {
    f"{sketchex.name} ({sketchex.min_xp} XP)": sketchex,
    f"{better_bank.name} ({better_bank.min_xp}XP)": better_bank
}

def bank(player):
    if not player.data["bank"]:
        print(colored("You need to join a bank!","red"))
        return join_bank_menu(player)
    portal_options = [
        {
            "type": "list",
            "name": "option",
            "message": f"Welcome to {player.data['bank'].name.capitalize()} interactive portal!",
            "choices": [
                {
                    "name": "Deposit"
                },
                {
                    "name": "Withdraw"
                },
                {
                    "name": "Leave Bank"
                },
                {
                    "name": "Bank Info"
                },
                {
                    "name": "⇠ Back"
                }
            ]
        }
    ]
    option = prompt(portal_options[0])["option"]
    handle_special(option, player)
    if option == "Bank Info":
        print_bank_info(player.data["bank"])
        return bank(player)
    elif option == "Leave Bank":
        player.data["money"] += player.data["bank_account"]
        print(colored("Withdrew ","cyan")+colored(f"${player.data['bank_account']}","green") + colored(f" from ", "cyan") +colored(player.data["bank"].name,"yellow"))
        player.data["bank_account"] = 0
        join_bank_menu(player)
        return bank(player)
    else:
        eval(f"{option.lower()}(player=player)")


def print_bank_info(bank):
    pt = PrettyTable()
    pt.title = bank.name
    pt.field_names = ["Interest Rate", "Initial Deposit Required",
                      "Minimum Deposit", "Minimum XP Needed"]
    pt.add_row([str(bank.interest_rate)+"%", "$"+str(bank.initial_deposit),
                "$"+str(bank.minimum_deposit), str(bank.min_xp)+" XP"])
    print(colored(pt,"blue"))

def confirm_action(message):
    confirm_question = [{
        "type": "confirm",
        "name": "confirmation",
        "message": message,
        "default": True
    }]
    return prompt(confirm_question)["confirmation"]

def join_bank_menu(player):
    banks = list(bank_dict.keys())
    banks = add_back(banks)
    bank_choices = [
        {
            "type": "list",
            "name": "item",
            "choices": [{"name": i} for i in banks],
            "message": "What bank would you like to sign with?"
        }
    ]
    b = prompt(bank_choices[0])["item"]
    handle_special(b, player)
    bank_final = bank_dict[b]
    print_bank_info(bank_final)
    if confirm_action(f"Are you sure you want to sign with {bank_final.name}?"):
        player.join_bank(bank_final)
        remove_special(banks, 1)
        return bank(player)
    else:
        return join_bank_menu(player)

def deposit(player):
    pbank = player.data["bank"]
    deposit_portal = [
        {
            "type": "input",
            "name": "option",
            "message": f"How much would you like to deposit into {pbank.name.capitalize()}?",
            "validate": lambda answer: validate_balance(player, answer),
            "filter": lambda answer: float(answer)
        }
    ]
    option = prompt(deposit_portal[0])["option"]
    if confirm_action(f"Are you sure you want to deposit ${option} to {pbank.name.capitalize()}?"):
        player.deposit(option)
    else:
        print(colored("You have canceled the transaction","red"))
    return bank(player)

def withdraw(player):
    pbank = player.data["bank"]
    withdraw_portal = [
        {
            "type": "input",
            "name": "option",
            "message": f"How much would you like to withdraw from {pbank.name.capitalize()}?",
            "validate": lambda answer: validate_balance(player, answer, False),
            "filter": lambda answer: float(answer)
        }
    ]
    option = prompt(withdraw_portal[0])["option"]
    if confirm_action(f"Are you sure you want to withdraw ${option} from {pbank.name.capitalize()}?"):
        player.withdraw(option)
    else:
        print(colored("You have canceled the transaction","red"))
    return bank(player)