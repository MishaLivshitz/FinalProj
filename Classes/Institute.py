from Classes import Lecturer


class Institute:

    def __init__(self, name, key, lec):
        self.name = name
        self.key = key
        self.lec = lec

    def __call__(self):
            print(self.key + ':' + self.name)
            for i in self.lec:
                print("     " + str(i.num) + ":" + i.name)
