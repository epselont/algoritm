# 69390387
import sys


class Deque:
    def __init__(self, max_len):
        self.__deque = [None] * max_len
        self.__max_size = max_len
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def push_back(self, item):
        if self.__size == self.__max_size:
            raise NotImplementedError
        self.__deque[self.__tail] = item
        self.__tail = (self.__tail + 1) % self.__max_size
        self.__size += 1

    def push_front(self, item):
        if self.__size == self.__max_size:
            raise NotImplementedError
        self.__deque[self.__head - 1] = item
        self.__head = (self.__head - 1) % self.__max_size
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            raise NotImplementedError
        item = self.__deque[self.__tail - 1]
        self.__deque[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_size
        self.__size -= 1
        return item

    def pop_front(self):
        if self.is_empty():
            raise NotImplementedError
        item = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_size
        self.__size -= 1
        return item


def command_deque(count, len_deque):
    deq = Deque(int(len_deque))
    for i in range(int(count)):
        line = sys.stdin.readline().rstrip()
        command, *value = line.split()
        if not value:
            try:
                print(*getattr(deq, command)())
            except NotImplementedError:
                print('error')
        else:
            try:
                getattr(deq, command)(value)
            except NotImplementedError:
                print('error')


def main():

    count = sys.stdin.readline().rstrip()
    len_deque = sys.stdin.readline().rstrip()
    command_deque(count, len_deque)


if __name__ == '__main__':
    main()
