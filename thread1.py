import os,time
from threading import Thread
def task():
    ret = 0
    for i in range(100000000):
        ret *= i
def iotask():
    f = open('tmp.txt','w')

if __name__ == "__main__":
    arr = []
    print('本机为',os.cpu_count,'核cpu')
    start = time.time()
    for i in range(5):
        # p = Thread(target=task)
        p = Thread(target=iotask)
        arr.append(p)
        p.start()
    for p in arr:
        p.join()
    stop = time.time()
    print('多线程耗时%s' %(stop-start))