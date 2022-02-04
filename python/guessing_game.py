"""
Defines a GuessingGame class.
"""
import re

class GuessingGame():
    """
    Accepts a number. If the guess function is called, it replies high/low/correct. Sets itself
    to correct if the correct number is supplied.
    Game is then over and a new class instance should be created.
    """
    def __init__(self, num):
        self.num = num
        self.solved = False

    def guess(self, num):
        """
        Attempts best effort to convert given guess to a decimal number. Returns low/high/correct
        and then sets solved if it's correct
        """
        try:
            num = int(num)
        except ValueError:
            # replace anything not a number in the text
            num = re.sub(r"[^0-9]", "", num)
            num = 0 if len(num) == 0 else int(num)

        # low guess
        if self.num > num:
            return "low"
        # high guess
        if self.num < num:
            return "high"
        # correct guess
        self.set_solved()
        return "correct"

    def set_solved(self):
        """
        Only sets solved to True
        """
        self.solved = True
