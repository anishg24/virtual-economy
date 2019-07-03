from random import uniform, choice

default_messages = {
    "risk":["Your boss caught you sleeping on the job"],
    "success": ["You did your work and got paid"],
    "young": "You are too young for this job",
    "unexperienced": "You don't have enough experience for this job"
    }

class Job:
    def __init__(self, name, payout_range, xp_needed, min_age, xp_range, risk_max, message=default_messages):
        self.name = name
        self.payout_min, self.payout_max = payout_range
        self.xp_needed = xp_needed
        self.xp_min, self.xp_max = xp_range
        self.min_age = min_age
        self.risk_max = risk_max
        self.messages = message 
    
    def calculate_payouts(self):
        self.payout = round(uniform(self.payout_min, self.payout_max),2)
        self.xp_out = round(uniform(self.xp_min,self.xp_max),2)
        return self.payout, self.xp_out
    
    def punish_player(self):
        pass