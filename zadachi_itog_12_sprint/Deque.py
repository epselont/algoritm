# 69374346
import sys


class Deque:
    def __init__(self, max_len):
        self.deque = [None] * max_len
        self.max_size = max_len
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push_back(self, item):
        if self.size == self.max_size:
            raise NotImplementedError
        self.deque[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size
        self.size += 1

    def push_front(self, item):
        if self.size == self.max_size:
            raise NotImplementedError
        self.deque[self.head - 1] = item
        self.head = (self.head - 1) % self.max_size
        self.size += 1

    def pop_back(self):
        if self.is_empty():
            raise NotImplementedError
        item = self.deque[self.tail - 1]
        self.deque[self.tail - 1] = None
        self.tail = (self.tail - 1) % self.max_size
        self.size -= 1
        return item

    def pop_front(self):
        if self.is_empty():
            raise NotImplementedError
        item = self.deque[self.head]
        self.deque[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return item


def command_deque(count, len_deque):
    deq = Deque(int(len_deque))
    for i in range(int(count)):
        command = sys.stdin.readline().rstrip()
        command = list(command.split())
        if command[0] == 'pop_back':
            try:
                print(deq.pop_back())
            except NotImplementedError:
                print('error')
        elif command[0] == 'pop_front':
            try:
                print(deq.pop_front())
            except NotImplementedError:
                print('error')
        elif command[0] == 'push_back':
            try:
                deq.push_back(command[1])
            except NotImplementedError:
                print('error')
        elif command[0] == 'push_front':
            try:
                deq.push_front(command[1])
            except NotImplementedError:
                print('error')


def main():

    count = sys.stdin.readline().rstrip()
    len_deque = sys.stdin.readline().rstrip()
    command_deque(count, len_deque)


if __name__ == '__main__':
    main()
