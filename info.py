#AUTHOR:    JASON ABRAMS

import os

class Information():

    def __init__(self):
        super().__init__()
        self.AUTHOR = "JASON ABRAMS"
        self.CREATION_DATE = "May 4, 2020"
        self.NOTE = ()
        self.TOKEN = ''

    def Get_Token(self):
        FN = 'token.txt'

        path = os.path.abspath(os.path.dirname(__file__))

        file_path = os.path.join(path, FN)

        info = open(file_path, "r")
        print(info)
        info.close() 
        self.TOKEN = info
        return self.TOKEN

