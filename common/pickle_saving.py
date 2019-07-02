import pickle
import os
from common.input_validation import get_input
from common.list_printer import print_list

os.chdir("saves/")

def create_player():
    data = {
        "name": get_input(str, "What is your name?\n> "),
        "age": get_input(int, "How old are you?\n> "),
        "gender": get_input(str, "What is your gender?\n> "),
        "xp": 0,
        "money": 500,
        "bank": 2500
    }
    confirm = get_input(bool, "Is this information correct?\n> ")
    if confirm:
        return Player(data) 
    else:
        while not confirm:
            a = list(data.keys())[:3]
            print_list(a)
            x = get_input(list, f"\nWhat would you like to change?", a)
            data[a[x]] = get_input(
                type(data[a[x]]), f"What would you like change this to?\n> ")
            print(f"Changed your {a[x]} to {data[a[x]]}.")
            confirm = get_input(bool, "Is this information correct?\n> ")
        return Player(data)

def read_savefile(file_name):
    try:
        with open(file_name, 'rb') as f:
            data = pickle.load(f)
    except FileNotFoundError:
        print("There doesn't seem to be a file to play with. Let's make one!")
        with open(create_player().file_name, 'rb') as f:
            data = pickle.load(f)
    return data

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
            pickle.dump(self.data, f)
        print(f"Updated \"{self.file_name}\"")

    def edit(self):
        confirm = False
        while not confirm:
            a = list(self.data.keys())[:3]
            print_list(a)
            x = get_input(list, f"\nWhat would you like to change?", a)
            self.data[a[x]] = get_input(
                type(self.data[a[x]]), f"What would you like change this to?\n> ")
            print(f"Changed your {a[x]} to {self.data[a[x]]}.")
            confirm = get_input(bool, "Is this information correct?\n> ")
        self.save()
    
