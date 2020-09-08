import os,time
from multiprocessing import Process
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
        # p = Process(target=task)
        p = Process(target=iotask)
        arr.append(p)
        p.start()
    for p in arr:
        p.join()
    stop = time.time()
    print('多进程耗时%s' %(stop-start))