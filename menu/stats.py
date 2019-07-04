import menu.main_menu as menu
from prettytable import PrettyTable


def stats(player):
    data = player.data
    pt = PrettyTable()
    pt.field_names = ["Money", "Bank Account", "Experience","Jobs Worked"]
    pt.add_row(["$"+str(data["money"]),"$"+str(data["bank_account"]), str(data["xp"])+ " XP", str(data["jobs_worked"])+" jobs"])
    print(pt)
    menu.main_menu(player=player)