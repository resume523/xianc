import threading
g_num=0
lock=threading.Lock()
def task1():
    lock.acquire()
    for i in range(100000):
        global g_num
        g_num=g_num+1
    print("task1",g_num)
    lock.release()
def task2():
    lock.acquire()
    for i in range(100000):
        global g_num
        g_num=g_num+1
    lock.release()
    print("task1",g_num)
if __name__ == '__main__':
    first_thread=threading.Thread(target=task1)
    second_thread = threading.Thread(target=task1)
    first_thread.start()
    second_thread.start()
