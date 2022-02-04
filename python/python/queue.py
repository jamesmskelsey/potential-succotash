class Queue:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Queue and a 'queue' value which is an array of stored values in the Queue
    def __init__(self) -> None:
        self.total = 0
        self.queue = []

    def __repr__(self) -> str:
        return str(self.queue)

    def enqueue(self, data):
        # write your code to add data to the Queue following FIFO and return the Queue
        self.queue.append(data)
        self.total += 1
        return self

    def dequeue(self):
        # write your code to removes the data to the Queue following FIFO and return the Queue
        if self.total > 0:
            self.total -= 1
            self.queue.pop(0)
            return self
        
        return self

    def size(self):
        # write your code that returns the size of the Queue
        return self.total

# Simple tests to make sure it works.
# q = Queue()

# for i in range(5):
#     q.enqueue(i)
# print(q)

# for i in range(6):
#     print(q.dequeue(), q.size())
# print(q)