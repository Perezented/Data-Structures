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
    def _search(self, target, currentNode):
        if target == currentNode.value:
            return True
        elif target < currentNode.value and currentNode.left is not None:
            return self._search(target, currentNode.left)
        elif target > currentNode.value and currentNode.right is not None:
            return self._search(target, currentNode.right)

    def contains(self, target):
        return self._search(target, self)

    # Return the maximum value found in the tree

    def searchMax(self, currentNode):
        if currentNode.right:
            return self.searchMax(currentNode.right)
        if currentNode.right is None:
            return currentNode.value

    def get_max(self):
        return self.searchMax(self)

    # Call the function `fn` on the value of each node

    def for_each(self, fn):

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

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
