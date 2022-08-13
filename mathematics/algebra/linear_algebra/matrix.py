class Matrix:
    def __init__(self, list_of_lists):
        """Takes a list of lists and then validates it."""
        self.values = list_of_lists
        self.order = str(len(list_of_lists)) + "/" + str(len(list_of_lists[0]))
        temp = len(self.values[0])
        for item in list_of_lists:
            if len(item) != temp:
                raise ArithmeticError

    def __str__(self):
        """Returns the string of the list of lists"""
        return str(self.values)

    def pretty_print(self):
        """
        Pretty prints the Matrix
        """
        for row in self.values:
            for item in row:
                print(item, end=" ")
            print()

    def determinant(self):
        total = 0
        negative = False
        first_row = self.values[0]
        for i in first_row:
            if negative:
                total -= i*Matrix([])
            else:
                total += i*Matrix([]).determinant()
            negative = not negative
        return total
