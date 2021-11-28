import datetime


def validate_thing_amount(user_input):
    try:
        user_input = int(user_input)

    except:
        return False

    if user_input in range(1, 5):
        return user_input
    else:
        return False


def validate_month_amount(user_input):
    try:
        user_input = int(user_input)

    except:
        return False

    if user_input in range(1, 7):
        return user_input
    else:
        return False


def validate_weeks_amount(user_input):
    try:
        user_input = int(user_input)

    except:
        return False

    if user_input in range(1, 5):
        return user_input
    else:
        return False


def validate_size_cell(user_input):
    try:
        user_input = int(user_input)

    except:
        return False

    if user_input in range(1, 11):
        return user_input

    return False


def validate_cell_period(user_input):
    try:
        user_input = int(user_input)

    except:
        return False

    if user_input in range(1, 13):
        return user_input
    else:
        return False


def validate_user_name(user_name):
    """Validate if user's name doesn't contain any numbers"""
    try:
        if not any(letter.isdigit() for letter in user_name):
            return True
    except:
        pass
    return False


def validate_user_birthday(user_birthday):
    """Validate if user's birthday matches the format dd.mm.yyyy."""
    try:
        datetime.datetime.strptime(user_birthday, '%d.%m.%Y')
        return True
    except:
        return False
