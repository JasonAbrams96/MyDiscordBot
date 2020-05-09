#AUTHOR:    JASON ABRAMS

import os

class Information:

    def __init__(self):
        super().__init__()
        self.AUTHOR = "JASON ABRAMS"
        self.CREATION_DATE = "May 4, 2020"
        self.NOTE = ()
        self.path = os.path.abspath(os.path.dirname(__file__))

    def Get_Token(self):
        FN = 'token.txt'

        file_path = os.path.join(self.path, FN)

        info = open(file_path, "r") 
        t = info.readline()
        info.close()
        return t

    def Get_Giphy_TOKEN(self):
        FN = 'giphy_key.txt'

        file_path = os.path.join(self.path, FN)
        info = open(file_path, "r")
        t = info.readline()
        info.close()
        return t


