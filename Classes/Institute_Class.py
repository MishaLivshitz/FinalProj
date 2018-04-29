from Classes import Lecturer_Class


class Institute:

    def __init__(self, name, key, lec):
        self.name = name
        self.key = key
        self.lec = lec

    def print_lec(self):
        lec_list = list(self.lec)
        print(lec_list)

