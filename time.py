import time
def caltime():
    item = 1
    for i in range(1,100000):
        item = item + i
    return item
starttime = time.time()
result = caltime()
endtime = time.time()
print('计算结果：'+str(result))
print('执行时间:'+str(endtime-starttime))