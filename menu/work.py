from menu.job import Job
from common.list_printer import print_objects
from common.input_validation import get_input
import menu.main_menu as menu

allowance = Job("Allowance",(0,10),0,0,(0,1),0)

def work(player,jobs=[allowance]):
    print("Jobs available:")
    print_objects(jobs)
    job = get_input(list, f"\nWhat would you like to do?", jobs)
    player.do_job(jobs[job])
    return menu.main_menu(player=player)
    
    
    
