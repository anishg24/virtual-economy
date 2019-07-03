from menu.job import Job
from common.common_options import *
import menu.main_menu as menu
from PyInquirer import *

# Job(self, name, payout_range, xp_needed, min_age, xp_range, risk_max, message=default_messages)

allowance = Job("Allowance",(0,10),0,0,(0,1),0)
chores = Job("Chores",(5,10),3,0,(1,2),0)

jobs_list = {
    allowance.name: allowance,
    chores.name : chores
}

def work(player,jobs=list(jobs_list.keys())):
    jobs = add_special(jobs)
    job_choices = [
        {
            "type": "list",
            "name": "job",
            "choices": [{"name": i} for i in jobs],
            "message": "What job would you like to take on?"
        }
    ]
    job = prompt(job_choices)["job"]
    handle_special(job, player)
    player.do_job(jobs_list[job])
    for _ in range(0,2):
        del jobs[-1]
    return menu.main_menu(player=player)
    
    
    
