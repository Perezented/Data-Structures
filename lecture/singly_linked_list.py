# creation of Node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def add_to_tail(self, value):
        # 1 create the Node from the value
        new_node = Node(value)
        # empty head and empty tail
        if self.head is None and self.tail is None:
            # in a one-element linked list, what should the head and tail be referring to?
            self.head = new_node
            # set the new node ot be the tail
            self.tail = new_node
        else:
            # 2 set the old tail's next to refer to the new Node
            self.tail.set_next(new_node)
            # 3 reassign self.tail to refer to the new Node
            self.tail = new_node

    def remove_head(self):
        # if we have an empty linked list
        if self.head is None and self.tail is None:
            return
        # if we have a linked list
        if not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.get_value()
        val = self.head.get_value()
        self.head = self.head.get_next()
        return val

    def remove_tail(self):
        # if we have an emply linked list
        if self.head is None and self.tail is None:
            return
        # if we have a non empty list
        # set the tail to be none
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
        val = self.tail.get_value() 
        # move self.tail to the Node right before
        self.tail = current
        return val

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we traverse the list
        current = self.head
        # check to see if we're at a valid node 
        while current:
            # return True if the current value we're looking at matches our target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def get_max(self):
        if not self.head:
            return None
        # reference to the largest value we've seen so far
        max_value = self.head.get_value()
        # reference to our current node as we traverse the list
        current = self.head.get_next()
        # check to see if we're still at a valid list node
        while current:
            # check to see if the current value is greater than the max_value
            if current.get_value() > max_value:
                # if so, update our max_value variable
                max_value = current.get_value()
            # update the current node to the next node in the list
            current = current.get_next()
        return max_value


ll = Node(1)
ll.next = Node(2)
ll.next.set_next(Node(3))
ll.next.next.set_next(Node(4))
ll.next.next.next.set_next(Node(5))
