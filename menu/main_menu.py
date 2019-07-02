from common.input_validation import *
from common.list_printer import print_list
from menu.work.work import work

def main_menu(data, options=["work","shop","settings","quit"]):
    print(data.data)
    print("Hello " + data["name"].capitalize() + "!\n")
    print_list(options, end="   ")
    action = get_input(list, f"\nWhat would you like to do?", options)
    eval(f"{options[action]}()")
 