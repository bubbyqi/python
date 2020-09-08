import os,time
def task():
    ret = 0
    for i in range(100000000):
        ret *= i
def iotask():
    f = open('tmp.txt','w')

if __name__ == "__main__":
    print('本机为',os.cpu_count,'核cpu')
    start = time.time()
    for i in range(5):
        # task()
        iotask()
    stop = time.time()
    print('单线程耗时%s' %(stop-start))