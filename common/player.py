from __future__ import print_function, unicode_literals
import pickle
import os
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
        "bank": 2500
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
    
    def do_job(self, job):
        if 0 < randrange(100) <= job.risk_max:
            return job.punish_player()
        elif self.data["age"] < job.min_age:
            return print(job.messages["young"])
        elif self.data["xp"] < job.xp_needed:
            return print(job.messages["unexperienced"])
        else:
            money, xp = job.calculate_payouts()
            self.data["money"] += money
            self.data["xp"] += xp
            return print(f"You have earned ${money} and {xp} XP")
    
    def backup(self):
        with open(self.file_name, "wb") as f:
            pickle.dump(self,f)
        print("Saved your data!")
