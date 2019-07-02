def get_input(wanted_type, message, given_list=None):
    if wanted_type == str:
        given = input(message)
        error_message = "\nEnter a valid string!"
        repeat = True
        while repeat:
            try:
                float(given)
                print(error_message)
                given = input(message)
                repeat = True
            except ValueError:
                repeat = False
        return given
    elif wanted_type == bool:
        given = input(message)
        true_keywords = ["true", "1", "t", "yes", "y"]
        false_keywords = ["false", "0", "f", "no", "n"]
        x = given.lower().strip()
        while x not in true_keywords + false_keywords:
            print("\nPlease enter a boolean value!")
            given = input(message)
            x = given.lower().strip()
        if x in true_keywords:
            return True
        elif x in false_keywords:
            return False
    elif wanted_type == list:
        if len(given_list) > 1:
            message = f"{message}\n(1-{len(given_list)}) > "
        else:
            message = f"{message}\n(1) > "
        x = get_input(int, f"{message}")
        while len(given_list) < x <= 0:
            print(f"Enter an integer between 1 and {len(given_list)}!")
            x = get_input(int, f"{message}")
        return x-1
    elif wanted_type == int:
        given = input(message)
        error_message = "\nEnter a valid integer!"
    elif wanted_type == float:
        given = input(message)
        error_message = "\nEnter a valid float!"
    while type(given) != wanted_type:
        try:
            x = f"{wanted_type}".split("'").pop(1)
            given = eval(f"{x}({given})")
        except NameError:
            print(error_message)
            given = input(message)
    return given