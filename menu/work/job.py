from common.list_printer import print_list
from random import randrange, uniform, choice

default_messages = {
    "risk":["Your boss caught you sleeping on the job"],
    "success": ["You did your work and got paid"],
    "young": "You are too young for this job",
    "unexperienced": "You don't have enough experience for this job"
    }

class Job:
    def __init__(self, name, payout_range, exp_needed, min_age, exp_range, risk_max, message=default_messages):
        self.name = name
        self.payout_min, self.payout_max = payout_range
        self.exp_needed = exp_needed
        self.exp_min, self.exp_max = exp_range
        self.min_age = min_age
        self.risk_max = risk_max
        self.messages = message 
        self.payout = round(uniform(self.payout_min, self.payout_max),2)
        self.exp_out = round(uniform(self.exp_min,self.exp_max),2)
