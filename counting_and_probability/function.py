"""The function class"""


class Function:
    """
    Function class
    """

    def __init__(self, function):
        breaker = []
        for item in function:
            if item != " ":
                breaker.append(item)
        right_hand_side = ""
        left_hand_side = ""
        left = True
        for item in breaker:
            if item == "=":
                left = False
            elif left:
                left_hand_side += item
            else:
                right_hand_side += item

        self.function = function

    def solve(self, number):
        """solves the function for a given number"""
        ans = ""
        for item in self.function:
            if item.isalpha:
                ans = ans + number
            else:
                ans = ans + item
        return int(ans)
