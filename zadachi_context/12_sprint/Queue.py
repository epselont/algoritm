import sys


class Queue:
    def __init__(self, max_len):
        self.deque = [None] * max_len
        self.max_size = max_len
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, item):
        if self.size == self.max_size:
            raise NotImplementedError
        self.deque[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise NotImplementedError
        item = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise NotImplementedError
        return self.deque[self.head]


def command_deque(count, len_deque):
    que = Queue(int(len_deque))
    for i in range(int(count)):
        command = sys.stdin.readline().rstrip()
        command = list(command.split())
        if command[0] == 'pop':
            try:
                print(que.pop())
            except NotImplementedError:
                print('None')
        elif command[0] == 'push':
            try:
                que.push(command[1])
            except NotImplementedError:
                print('error')
        elif command[0] == 'peek':
            try:
                print(que.peek())
            except NotImplementedError:
                print('None')
        elif command[0]:
            print(que.size)


def main():

    count = sys.stdin.readline().rstrip()
    len_deque = sys.stdin.readline().rstrip()
    command_deque(count, len_deque)


if __name__ == '__main__':
    main()
