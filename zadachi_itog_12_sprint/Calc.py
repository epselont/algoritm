# 69390248
import sys

COMMAND = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: y - x,
    '/': lambda x, y: y // x,
    '*': lambda x, y: x * y
}


class Stack:
    def __init__(self):
        self.__stack = []

    def is_empty(self):
        return self.__stack == 0

    def push(self, item):
        self.__stack.append(int(item))

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.__stack.pop()


def calc(line):
    stack = Stack()
    line_input = list(line.split())
    for val in line_input:
        if val in COMMAND.keys():
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(COMMAND[val](num1, num2))
        else:
            stack.push(int(val))

    return stack.pop()


def main():

    line = sys.stdin.readline().rstrip()
    print(calc(line))


if __name__ == '__main__':
    main()
