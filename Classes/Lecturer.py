class Lecturer:

    def __init__(self, num, name):
        self.num = num
        self.name = name

    def __call__(self):
        print(self.number + ':' + self.name)

