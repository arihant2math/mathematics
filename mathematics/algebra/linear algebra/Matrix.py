class Matrix:
    def __init__(self, list_of_lists):
        self.values = list_of_lists
        self.order = str(len(list_of_lists)) + "/" + str(len(list_of_lists[0]))
        temp = len(self.values[0])
        for item in list_of_lists:
            if len(item) != temp:
                raise ArithmeticError

    def __str__(self):
        return ""

    def pretty_print(self):
        """
        Pretty prints the Matrix
        """
        for row in self.values:
            for item in row:
                print(item, end=" ")
            print()
