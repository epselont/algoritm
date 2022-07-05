
from random import randint


def main():

    with open('test_1.txt', 'w') as f:
        f.write('1000000\n')
        for i in range(1000000):
            x = randint(0, 100)
            f.write(str(x) + ' ')


if __name__ == '__main__':
    main()
