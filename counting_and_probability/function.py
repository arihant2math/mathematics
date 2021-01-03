class function:
    def __init__(self, function):
        self.function = function

    def solve(self, number, function):
        ans = ""
        for item in function:
            if item.isalpha:
                ans = ans + number
            else:
                ans = ans + item
        return int(ans)
