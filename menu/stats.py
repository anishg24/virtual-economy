import menu.main_menu as menu
from prettytable import PrettyTable
from colorama import init
from termcolor import colored
init()

def stats(player):
    data = player.data
    pt = PrettyTable()
    pt.field_names = ["Money", "Bank Account", "Age", "Experience",
                      "Jobs Worked", "Years", "Months"]
    pt.add_row(["$"+str(data["money"]), "$"+str(data["bank_account"]), str(data["age"])+" years", str(data["xp"]) +
                " XP", str(data["jobs_worked"])+" jobs", str(data["years"]), str(data["months"])])
    print(colored(pt,"blue"))
    menu.main_menu(player=player)
