from __future__ import print_function, unicode_literals
import pickle
import os
import time
from random import randrange
from common.value_validator import *
from PyInquirer import *
from colorama import init
from termcolor import colored
init()

os.chdir("saves/")


def edit_questions(data):
    ok = False
    questions = [
        {
            "type": "list",
            "message": "What do you want to edit?",
            "name": "edit_choice",
            "choices": [{"name": i.capitalize()} for i in list(data.keys())[:3]],
            "validator": lambda answer: check_edit(answer)
        },
        {
            "type": "input",
            "message": "What do you want to change this to?",
            "name": "changed_val"
        },
        {
            "type": "confirm",
            "name": "confirm",
            "message": "Is this information correct?",
            "default": True
        },
        {
            "type": "input",
            "message": "What do you want your new age to be?",
            "name": "age",
            "validate": lambda answer: validate_age(answer),
            "filter": lambda answer: int(answer)
        }
    ]
    while not ok:
        x = prompt(questions[0])["edit_choice"]
        if x == "Age":
            data[x.lower()] = prompt(questions[3])["age"]
        else:
            data[x.lower()] = prompt(questions[1])["changed_val"]
        ok = prompt(questions[2])["confirm"]


def create_player():
    questions = [
        {
            "type": "input",
            "name": "name",
            "message": "What's your name?"
        },
        {
            "type": "input",
            "name": "age",
            "message": "What's your age?",
            "validate": lambda answer: validate_age(answer),
            "filter": lambda answer: int(answer)
        },
        {
            "type": "input",
            "name": "gender",
            "message": "What's your gender?"
        },
        {
            "type": "confirm",
            "name": "confirm",
            "message": "Is this information correct?",
            "default": True
        }
    ]
    answers = prompt(questions)
    data = {
        "name": answers["name"],
        "age": answers["age"],
        "gender": answers["gender"],
        "xp": 0,
        "money": 500,
        "bank_account": 0,
        "bank": None,
        "jobs_worked": 0,
        "inventory": {},
        "years": 0,
        "months": 0,
        "monthly_jobs": 5,
    }
    confirm = answers["confirm"]
    if not confirm:
        edit_questions(data)
    return Player(data)


def read_savefile(file_name):
    try:
        with open(file_name, 'rb') as f:
            player = pickle.load(f)
    except FileNotFoundError:
        print("There doesn't seem to be a file to play with. Let's make one!")
        with open(create_player().file_name, 'rb') as f:
            player = pickle.load(f)
    return player


class Player:
    def __init__(self, data):
        self.data = data
        self.max_jobs = 5
        self.save()

    def save(self):
        counter = 0
        self.file_name = self.data["name"].lower().split()[
            0] + str(self.data["age"])
        items = os.listdir()
        for i in items:
            if i.split("-")[0] == self.file_name:
                counter += 1
        self.file_name = self.file_name + f"-{counter}.vecon"
        with open(self.file_name, 'wb') as f:
            pickle.dump(self, f)
        print(colored(f"Updated \"{self.file_name}\"","cyan"))

    def edit(self):
        edit_questions(self.data)
        os.remove(self.file_name)
        self.save()

    def work(self, job):
        if 0 < randrange(100) <= job.risk_max:
            return job.punish_player()
        elif self.data["age"] < job.min_age:
            return print(colored(job.messages["young"],"red"))
        elif self.data["xp"] < job.xp_needed:
            return print(colored(job.messages["unexperienced"],"red"))
        else:
            money, xp = job.calculate_payouts()
            self.data["jobs_worked"] += 1
            self.data["monthly_jobs"] -= 1
            self.data["money"] = round((self.data["money"] + money), 2)
            self.data["xp"] = round((self.data["xp"] + xp), 2)
            x = self.data["monthly_jobs"]
            print(colored("You have earned","cyan") + colored(' $'+str(money), 'green') + colored(" and ", "cyan") 
            + colored(str(xp)+'XP','green'))
            print(colored("You can work ","cyan") + colored(x,'yellow') + colored(" more times this month!","cyan"))

    def backup(self):
        with open(self.file_name, "wb") as f:
            pickle.dump(self, f)
        print(colored("Saved your data!","green"))

    def buy(self, item, amount):
        cost = amount * item.cost
        if self.data["age"] < item.min_age:
            return print(colored("You are too young to buy this item!","red"))
        elif self.data["money"] < cost:
            return print(colored("You don't have enough money for this item!","red"))
        else:
            self.data["money"] = round(self.data["money"]-cost, 2)
            self.data["money"] = round(self.data["money"])
            try:
                # {item.name: [count, [items]]}
                self.data["inventory"][item.name][0] += amount
                self.data["inventory"][item.name][1].append(item)
            except KeyError:
                self.data["inventory"][item.name] = [amount, [item]]
            return print(colored("You have bought ","cyan")+colored(str(amount)+f"x {item.name}","yellow") + colored(" for ","cyan") + colored("$"+str(cost)+"!","green"))

    def next_month(self):
        self.data["months"] += 1
        if self.data["months"] == 12:
            self.data["age"] += 1
            self.data["money"] += 50
            self.data["xp"] += 10
            print(colored("Happy Birthday!","magenta",attrs=["blink"]))
            print(colored("You have gained ","cyan")+colored("$50","green")+colored(" and ","cyan")+colored("10 XP","green"))
            self.data["months"] = 0
            self.data["years"] += 1
        # time.sleep(3)
        self.data["monthly_jobs"] = self.max_jobs
        print(colored("It is a new month and you feel relaxed! Get to working!","cyan"))
        if self.data["bank"]:
            self.data["bank_account"] *= 1 + (self.data["bank"].interest_rate/100)
            self.data["bank_account"] = round(self.data["bank_account"],2)
            print(colored("Your bank account has collected interest! You have a total of ","cyan") +
                  colored("$"+str(self.data["bank_account"]),"green")+colored(" in your bank account","cyan"))

    def join_bank(self, bank):
        if self.data["xp"] < bank.min_xp:
            return print(colored(f"You are too unexperienced to join {bank.name}!","red"))
        elif self.data["money"] < bank.initial_deposit:
            return print(colored(f"You don't have enough money to make an initial deposit of {bank.initial_deposit}!", "red"))
        else:
            self.data["bank"] = bank
            self.data["bank_account"] = bank.initial_deposit
            self.data["money"] -= bank.initial_deposit
            return print(colored("You joined ","cyan")+colored(bank.name,"yellow")+colored(" and deposited ", "cyan") + colored(f"${bank.initial_deposit}","red") + colored("!","cyan"))

    def change_bank(self, new_bank):
        pass

    def deposit(self, amount):
        if self.data["money"] >= amount:
            self.data["money"] -= amount
            self.data["bank_account"] += amount
            map(lambda x: round(x,2), [self.data["bank_account"], self.data["money"]])
            print(colored("You succesfully deposited ","cyan") + colored(f"${amount}!","green"))
        else:
            print(colored("You don't have enough money!", "red"))

    def withdraw(self, amount):
        if self.data["bank_account"] >= amount:
            self.data["bank_account"] -= amount
            self.data["money"] += amount
            map(lambda x: round(x,2), [self.data["bank_account"], self.data["money"]])
            print(colored("You successfully withdrew ", "cyan") + colored(f"${amount}!","green"))
        else:
            print(colored("You don't have enough money in your bank!", "red"))
