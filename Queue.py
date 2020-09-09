import queue
# q = queue.Queue()
q = queue.LifoQueue()
for index in  range(10):
    q.put(index)
while not q.empty():
    print(q.get(),end=',')