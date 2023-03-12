class stack:
    temp = []

    def __init__(self):
        self.top = -1

    def push(self, x):
        self.temp.append(x)
        self.top = self.top + 1

    def pop(self):
        if self.top != 0:
            self.top -= 1
        self.temp.pop()
        return self.temp[self.top]

    def empty(self):
        return True if self.top == 0 else False


if __name__ == '__main__':
    s = stack()
    s.push(10)
    s.push(20)
    s.push(30)
    s.push(40)

