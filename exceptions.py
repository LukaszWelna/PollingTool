class WrongValueException(Exception):
    """
    Handling exception when user choose unavailable answer option
    """
    def __init__(self, answer_value) -> None:
        super().__init__(f"{answer_value} is wrong value. Please choose option a, b, c or d")