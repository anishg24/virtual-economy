from menu.work.job import Job
from common.list_printer import print_objects
from common.input_validation import get_input

allowance = Job("Allowance",(0,10),0,0,(0,1),0)

def work(jobs=[allowance]):
    print("Jobs available:")
    print_objects(jobs)
    action = get_input(list, f"\nWhat would you like to do?", jobs)
    jobs[action]
    
    