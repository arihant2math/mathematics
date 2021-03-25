"""Holds a list, so it can be accessed when python quits"""


class HoldList:
    """
    Holds a list, so it can be accessed after python quits and starts again.
    """

    def __init__(self, hold, name):
        self.name = name
        try:
            f = open(name + ".list", "r")
            self.hold = f.read()
            f.close()
            self.write()
        except FileNotFoundError:
            self.hold = hold
            self.write()

    def delete(self):
        """Deletes the object, should be used with del"""
        import os
        os.remove(self.name + ".txt")

    def write(self):
        """Saves hold"""
        f = open(self.name + ".list", "w")
        f.write(str(self.hold)[1:len(self.hold)-2])
        f.close()

    def read(self):
        """
        Returns the contents of the file
        :return:
        """
        f = open(self.name + ".list", "r")
        contents = f.read().split(", ")
        f.close()
        return contents
