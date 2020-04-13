class Class():
    a = 1
    b = 2

    def __init__(self):
        # return 1
        pass

    def __del__(self):
        print(self.a)
        return 1

    def f(self):
        pass


c = Class()

