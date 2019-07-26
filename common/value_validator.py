from PyInquirer import Validator, ValidationError

def check_int(answer):
    try:
        int(answer)
        return True
    except ValueError:
        return False

def check_float(answer):
    try:
        float(answer)
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


def validate_amount(answer):
    if check_int(answer):
        return True
    else:
        raise ValidationError(
            message="Please enter a number!",
            cursor_position=len(answer)
        )

def validate_balance(player, answer, deposit=True):
    money = player.data["money"]
    money_in_bank = player.data["bank_account"]
    if check_float(answer):
        float_answer = float(answer)
        if float_answer == 0:
            raise ValidationError(
                message=f"You aren't allowed to {'deposit' if deposit else 'withdraw'} $0!"
            )
        if deposit:
            if money >= float_answer:
                return True
            else:
                raise ValidationError(
                    message=f"You don't have that much money! (You have ${money})",
                    cursor_position=len(answer)
                )
        else:
            if money_in_bank >= float_answer:
                return True
            else:
                raise ValidationError(
                    message=f"You don't have that much money in your bank! (You have ${money_in_bank})",
                    cursor_position=len(answer)
                )
    else:
        raise ValidationError(
            message="Please enter a valid number!",
            cursor_position=len(answer)
        )