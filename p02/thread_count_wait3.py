import _thread as thread
import time
stdoutmutex = thread.allocate_lock()
numthreads = 5
exitmutexes = [thread.allocate_lock() for i in range(numthreads)]


def counter(myID, count, mutex):
    for i in range(count):
        time.sleep(1 / (myID + 1))
        with mutex:
            print('[%s] => %s' % (myID, i))
    exitmutexes[myID].acquire()


for i in range(numthreads):
    thread.start_new_thread(counter, (i, 5, stdoutmutex))

while not all(mutex.locked() for mutex in exitmutexes):
    time.sleep(0.25)

print('Main thread exiting.')
