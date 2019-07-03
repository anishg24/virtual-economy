from menu.job import Job
from common.common_options import *
import menu.main_menu as menu
from PyInquirer import *

class Item:
    def __init__(self, name, cost, min_age):
        self.name = name
        self.cost = cost
        self.min_age = min_age
