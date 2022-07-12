import sys


class StackMax:
    def __init__(self):
        self.items = []
        self.max_num = []

    def push(self, item):
        if len(self.items) == 0:
            self.max_num.append(int(item))
        elif int(item) > self.max_num[len(self.items)-1]:
            self.max_num.append(int(item))
        else:
            self.max_num.append(self.max_num[len(self.items)-1])
        self.items.append(int(item))

    def pop(self):
        try:
            if len(self.items) >= 1:
                self.items.pop()
                self.max_num.pop()
            else:
                self.items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        try:
            print(self.max_num[len(self.items)-1])
        except:
            print(None)


def main():
    count = sys.stdin.readline().rstrip()
    count = int(count)
    stack = StackMax()
    for i in range(count):
        comand = sys.stdin.readline().rstrip()
        comand = list(comand.split())
        if comand[0] == 'pop':
            stack.pop()
        elif comand[0] == 'push':
            stack.push(comand[1])
        elif comand[0] == 'get_max':
            stack.get_max()


if __name__ == '__main__':
    main()
