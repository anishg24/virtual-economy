import menu.main_menu as menu
from prettytable import PrettyTable


def stats(player):
    data = player.data
    pt = PrettyTable()
    pt.field_names = ["Money", "Bank Account", "Experience"]
    pt.add_row(["$"+str(data["money"]),"$"+str(data["bank"]), str(data["xp"])+ " XP"])
    print(pt)
    menu.main_menu(player=player)