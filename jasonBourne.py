"""
This file returns the relative file structure so 
that you can always do file stuff on anyone's machine
"""

import os 

class bourne:
    def __init__(self, curFileDir):
        self.cwd = os.getcwd()
        self.home = os.path.expanduser("~")
        self.curFileDir = curFileDir

    def navigateToo(self, path):
        pathStr = path.split("/")
        for i in pathStr:
            if i == "..":
                self.cwd = "/".join(self.cwd.split("/")[:-1])
            else:
                self.cwd += "/" + i