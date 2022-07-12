# 69375105
import sys


class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == 0

    def push(self, item):
        self.stack.append(int(item))

    def pop(self):
        if self.is_empty():
            raise IndexError
        return self.stack.pop()


def Calc(line):
    stack = Stack()
    line_input = list(line.split())
    for val in line_input:
        if val == '+':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(num1 + num2)
        elif val == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(num2 - num1)
        elif val == '*':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(num1 * num2)
        elif val == '/':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.push(num2 // num1)
        else:
            stack.push(int(val))

    return stack.pop()


def main():

    line = sys.stdin.readline().rstrip()
    print(Calc(line))


if __name__ == '__main__':
    main()
