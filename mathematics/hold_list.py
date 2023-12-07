"""Holds a list, so it can be accessed when python quits"""
import os
from pathlib import Path


class HoldList:
    """
    Holds a list, so it can be accessed after python quits and starts again.
    """

    def __init__(self, name):
        """
        :param name: The name of the file, starts in the default directory
        """
        self.path = Path(Path.home()) / ".mathematics"
        self.file_name = self.path / (name + ".list")
        self.hold = []
        if self.path.exists():
            self._read()
        else:
            os.mkdir(self.path)
            self.save()

    def delete(self):
        """Deletes the file"""
        os.remove(self.file_name)

    def save(self):
        """Saves hold"""
        to_write = str(self.hold).replace(" ", "")
        f = open(self.file_name, "w")
        f.write(to_write[1 : len(to_write) - 1])
        f.close()

    def read(self):
        """
        Returns the contents of the file
        :return:
        """
        self._read()
        return self.hold

    def write(self, new):
        self.hold = new
        self.save()

    def append(self, item):
        self.hold.append(item)
        self.save()

    def _read(self):
        f = open(self.file_name, "r")
        self.hold = f.read().split(",")
        f.close()
