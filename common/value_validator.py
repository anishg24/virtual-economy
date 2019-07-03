from PyInquirer import Validator, ValidationError

def check_int(answer):
    try:
        int(answer)
        return True
    except ValueError:
        return False

def validate_age(answer):
    if check_int(answer):
        int_answer = int(answer)
        if 0 < int_answer < 100:
            return True
        else:
            raise ValidationError(
                message='Please enter an age between 0-100!',
                cursor_position=len(answer)
            )
    else:
        raise ValidationError(
            message='Please enter a valid number!',
            cursor_position=len(answer)
        )

def get_int(answer):
    return int(answer)
