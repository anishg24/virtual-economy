from __future__ import print_function, unicode_literals
import pickle
import os
import time
from random import randrange
from common.value_validator import *
from PyInquirer import *


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
        "bank": "",
        "jobs_worked": 0,
        "inventory": {},
        "days": 0,
        "jobs_today": 0,
        "job_daily_max": 3
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
        self.save()

    def save(self):
        counter = 0
        self.file_name = self.data["name"].lower().split()[0] + str(self.data["age"])
        items = os.listdir()
        for i in items:
            if i.split("-")[0] == self.file_name:
                counter += 1
        self.file_name = self.file_name + f"-{counter}.vecon"
        with open(self.file_name, 'wb') as f:
            pickle.dump(self, f)
        print(f"Updated \"{self.file_name}\"")

    def edit(self):
        edit_questions(self.data)
        os.remove(self.file_name)
        self.save()
    
    def work(self, job):
        if self.data["jobs_today"] >= self.data["job_daily_max"]:
            return print("You are too exhausted to work again today!")
        elif 0 < randrange(100) <= job.risk_max:
            return job.punish_player()
        elif self.data["age"] < job.min_age:
            return print(job.messages["young"])
        elif self.data["xp"] < job.xp_needed:
            return print(job.messages["unexperienced"])
        else:
            money, xp = job.calculate_payouts()
            self.data["money"] = round((self.data["money"] + money),2)
            self.data["xp"] = round((self.data["xp"] + xp),2)
            self.data["jobs_worked"] += 1
            self.data["jobs_today"] += 1
            jt = self.data["jobs_today"]
            jm = self.data["job_daily_max"]
            return print(f"You have earned ${money} and {xp} XP!\nYou can work {jm-jt} more times today!")
    
    def backup(self):
        with open(self.file_name, "wb") as f:
            pickle.dump(self,f)
        print("Saved your data!")
    
    def buy(self, item, amount):
        cost = amount * item.cost
        if self.data["age"] < item.min_age:
            return print("You are too young to buy this item!")
        elif self.data["money"] > cost:
            return print("You don't have enough money for this item!")
        else:
            self.data["money"] = round(self.data["money"]-cost,2)
            try:
                # {item.name: [count, [items]]}
                self.data["inventory"][item.name][0] += amount
                self.data["inventory"][item.name][1].append(item)
            except KeyError:
                self.data["inventory"][item.name] = [amount,[item]]
            return print(f"You have bought {amount}x \"{item.name}\" for ${cost}!")
    
    def next_day(self):
        self.data["days"] += 1
        if self.data["days"] >= 365:
            self.data["age"] += 1
            self.data["money"] += 50
            self.data["xp"] += 10
            print("Happy Birthday!\nYou have gained $50 and 10 XP")
        time.sleep(3)
        self.data["jobs_today"] = 0 
        print("It is a new day and you feel relaxed! Get to working!")
    
    def join_bank(self, bank):
        pass

    def change_bank(self, new_bank):
        pass
    
    def deposit(self):
        pass