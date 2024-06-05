from time import sleep
from threading import Thread


def print_numbers(start=1, end=10):
    for i in range(start, end + 1):
        print(i)
        sleep(1)


def print_a_letter(start='a', end='z'):
    for i in range(ord(start), ord(end) + 1):
        print(chr(i))
        sleep(1)


thread = Thread(target=print_numbers, kwargs=dict(start=1, end=10))
thread.start()

print_a_letter(start='a', end='j')

thread.join()
