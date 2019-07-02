def print_list(data, end="\n"):
    for i in range(0, len(data)):
        print(f"({i+1}) {data[i].capitalize()}", end=end)

def print_objects(list_of_objects, end="\n"):
    for i in range(0, len(list_of_objects)):
        print(f"({i+1}) {list_of_objects[i].name.capitalize()}", end=end)
