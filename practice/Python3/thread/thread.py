import threading
import time
import random


# base thread
class MyThread(threading.Thread):
    def run(self):
        # task implementation
        print("in my thread")


thread = MyThread()
thread.run()


# base thread without lock

def show_number_without_lock(number):
    wait_time = random.uniform(0, 0.5)
    time.sleep(wait_time)
    print(str(number) + ',')

thread_list = []
for n in range(1, 11):
    thread = threading.Thread(target=show_number_without_lock, args=[n])
    thread_list.append(thread)

for i in thread_list:
    i.start()
    # i.join()


time.sleep(2)
# base thread with lock
lock = threading.Lock()


def show_number_with_lock(number):
    with lock:
        wait_time = random.uniform(0, 0.5)
        time.sleep(wait_time)
        print(str(number) + ',')


for n in range(1, 11):
    threading.Thread(target=show_number_with_lock, args=(n,)).start()
