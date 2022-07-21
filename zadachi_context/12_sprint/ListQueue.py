import sys


class Queue:
    def __init__(self):
        self.queue = []
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def put(self, item):
        self.queue.append(item)
        self.tail = self.tail + 1
        self.size += 1

    def get(self):
        if self.is_empty():
            raise NotImplementedError
        item = self.queue[self.head]
        self.queue[self.head] = None
        self.head = self.head + 1
        self.size -= 1
        return item


def command_deque(count):
    que = Queue()
    for i in range(int(count)):
        command = sys.stdin.readline().rstrip()
        command = list(command.split())
        if command[0] == 'get':
            try:
                print(que.get())
            except NotImplementedError:
                print('error')
        elif command[0] == 'put':
            que.put(command[1])
        else:
            print(que.size)


def main():
    count = sys.stdin.readline().rstrip()
    command_deque(count)


if __name__ == '__main__':
    main()
