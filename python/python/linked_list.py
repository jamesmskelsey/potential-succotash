from stack import Stack

class LinkList:
    # write your __init__ method here that should store a 'head' value which the first Node in the LinkedList and a 'length' value which is the total number of Nodes in the LinkedList
    def __init__(self, data) -> None:
        self.head = Node(data)
        self.length = 1 # Start at one because we initialize with some data

    def __repr__(self) -> str:
        return str(self.print())

    def add(self, data):
        # write your code to ADD an element to the Linked List
        # start with the head
        # traverse the linked list until I get to one where next is none
        # put the new node there. return the linked list
        curr = self.head
        while curr.next:
            curr = curr.next
        self.length += 1
        curr.next = Node(data)

    def remove(self, index):
        # write your code to REMOVE an element and index from the Linked List
        # start with the head
        # hold on to the previous node
        # traverse until we are at the specified index and hold on to current
        # assign the previous node.next to curr.next - the item has been removed from the list.
        # short circuit
        # can't remove an index higher than our length
        # can't remove an index below 0
        if (index > self.length - 1 ) or index < - 1:
            return self
        # special case where we need to move the head to the second index
        if index == 0:
            self.head = self.head.next
            return self

        curr_index = 1
        prev = self.head
        curr = prev.next
        while curr_index < self.length:
            if curr_index == index:
                prev.next = curr.next
                self.length -= 1
                return self
        
            curr_index += 1
            temp, prev = curr, curr
            curr = temp.next
        return self
        
    def get(self, index):
        # write you code to GET and return an element from the Linked List
        curr_index = 0
        curr = self.head
        while curr_index < index:
            curr = curr.next
            curr_index += 1
        return curr.data

    def print(self):
        output = []
        curr = self.head
        while True:
            output.append(curr.data)
            curr = curr.next
            if curr == None:
                break
        return output

    def reverse(self):
        # place head node in to a stack
        stack = Stack()
        # push all of our nodes in to the stack
        curr = self.head
        while curr.next:
            stack.push(curr)
            curr = curr.next
        self.head = curr
        # pop all of them back out
        while stack.size():    
            curr.next = stack.pop()
            curr = curr.next
        curr.next = None
        

# ----- Node ------
class Node:
    # store your DATA and NEXT values here
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

    def __repr__(self):
        return f"data: {self.data}"

ll = LinkList(0)
ll.add(5)
ll.add(10)
ll.add(20)

print(ll)
ll.reverse()
print(ll)