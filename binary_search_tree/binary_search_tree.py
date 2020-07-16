"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the node
        # if value < Node 's Value
        if value < self.value:
            # we need to go left
            if self.left is None:
            # if there is no left child, then we can wrap the value
            #  in a BSTNode and park it
                self.left = BSTNode(value)
            else:
            # otherwise there is a child
            # call the left child's `insert` method
                self.left.insert(value)

        # otherwise, value > = Node's value
        else:
            # we need to go right
            if self.right is None:
            # if there is right child, then we can wrap the value
            #  in a BSTNode and park it 
                self.right = BSTNode(value)
            # call the right child's `insert` method
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        return self._search(target, self)

    def _search(self, target, currentNode):
        # if the current node is the target
        if target == currentNode.value:
            # return True
            return True
            # else if the target is less then the current node and there is a left node
        elif target < currentNode.value and currentNode.left is not None:
            # return this search on the target and left Node
            return self._search(target, currentNode.left)
            # else if the target is more then the current node and there is a right node
        elif target > currentNode.value and currentNode.right is not None:
            # return this search on the target and right Node
            return self._search(target, currentNode.right)

    ################################################
    # def contains(self, target):
    #     # 1. base case
    #     # if the value of this node matches the target, then we have found what we are lookin for
    #     if self.value == target:
    #         return True
    #     # 2. how do we move closer to the base case? 
    #     # compare the target againsts this node's value ot determine which direction we need to go in 
    #     if target < self.value:
    #         # we need to go left
    #         # what if there is no left child?
    #         if not self.left:
    #             return False
    #         else:
    #             # call contains on left 
    #             self.left.contains(target)
    #     if target > self.value:
    #         # we need to go right
    #         # what if there is no right child?

    #         if not self.right:
    #             return False
    #         else:
    #             # call contains on right 
    #             self.right.contains(target)
    ################################################
    # Return the maximum value found in the tree
    def searchMax(self, currentNode):
        if currentNode.right:
            return self.searchMax(currentNode.right)
        if currentNode.right is None:
            return currentNode.value

    def get_max(self):
        return self.searchMax(self)

################################################
    # def get_max(self):
    #     # the max value in the tree will always be the right most value
    #     # recursive
    #     # just keep going right until there is no right child node
    #     # base case:
    #     if not self.right:
    #         return self.value
    #         # otherwise call get max on right child
    #     elif self.right:
    #         return getmax(self.right)
################################################
    # Call the function `fn` on the value of each node
    # def runEach(self, value, fn):
    #     if value.value is not None:
    #         fn(value.value)
    #     if value.left is not None:
    #         fn(value.left)
    #         self.runEach(value, fn)
    #     if value.right is not None:
    #         value = value.right
    #         self.runEach(value, fn)

    def for_each(self, fn):
        # run the function on the first value
        fn(self.value)
        # if there is a left
        if self.left:
            # run it on left
            self.left.for_each(fn)
        # if there is a right
        if self.right:
            # run it on right
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we will use a stack
        stack = []
        stack.append(self)
        # so long a s our stack has nodes in it, theses more nodes to taverse
        while len(stack) > 0:
            # pop the tiop node from the stack
            current = stack.pop()

            # add the current node's right child
            if current.right:
                stack.append(current.right)
            # add the current node's left child
            if current.left:
                stack.append(current.left)
            # call the anon function
            fn(current.value)

    def iterative_breadth_first_for_each(self, fn):
        from collections import deque
        # bft: fifo
        # we will use a queue to facilitate the ordering
        queue = deque()
        queue.append(self)
        # continue to travese so long tas ther eare nodes in the queue
        while len(queue > 0):
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
            fn(current.value)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        if node.left is not None:
            self.in_order_print(node.left)
        print(node.value)
        if node.right is not None:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        print(node.value)
        if node.left is not None:
            self.bft_print(node.left)
        if node.right is not None:
            self.bft_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
