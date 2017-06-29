"Use multiprocessing to start independent programs, os.fork or not"

import os
from multiprocessing import Process


def runprogramm(arg):
    os.execlp('python3', 'python3', 'child.py', str(arg))


if __name__ == '__main__':
    for i in range(5):
        Process(target=runprogramm, args=(i,)).start()
    print('parent exit.')
