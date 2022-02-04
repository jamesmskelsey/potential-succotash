class Stack:
    # write your __init__ method here that should store a 'total' value which is the total number of elements in the Stack and a 'stack' value which is an array of stored values in the Stack
    def __init__(self) -> None:
        self.total = 0
        self.stack = []

    def __repr__(self):
        return str(self.stack)

    def push(self, data):
        # write your code to add data following LIFO and return the Stack
        self.total += 1
        self.stack.append(data)
        return self

    def pop(self):
        # write your code to removes the data following LIFO and return the Stack
        if self.total > 0:
            data = self.stack.pop(-1)
            self.total -= 1
            print("popping from stack: ", data)
        return data

    def size(self):
        # write your code that returns the size of the Stack
        return self.total

# s = Stack()

# for i in range(5):
#     print(s, s.size())
#     s.push(i)


# while s.size() > 0:
#     print(s, s.size())
#     s.pop()

# print(s, s.size())

