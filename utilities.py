from exceptions import WrongValueException

def check_user_answer(answer: str) -> bool:
    """
    Check if chosen answer option by user is available
    """
    if answer in {'a', 'b', 'c','d'}:
        return True
    raise WrongValueException(answer)