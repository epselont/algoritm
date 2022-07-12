import sys


class StackMax:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        try:
            self.items.pop()
        except IndexError:
            print('error')

    def get_max(self):
        try:
            print(max(self.items))
        except ValueError:
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
