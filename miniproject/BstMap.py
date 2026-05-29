from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        if key == self.key:
            self.value = value
        elif key < self.key:  # if its smaller adds it to the left subtree
            if self.left is None:  # check if there is a left child
                self.left = Node(key, value)
            else:
                self.left.put(key, value)  # add to existing node
        else:  # if its larger adds it to the right subtree
            if self.right is None:  # check if there is a right child
                self.right = Node(key, value)
            else:
                self.right.put(key, value)

    def to_string(self):
        new_string = ""
        if self.left is not None:
            new_string += self.left.to_string()
        new_string += f"({self.key}, {self.value}) "
        if self.right is not None:
            new_string += self.right.to_string()
        return new_string

    def count(self):
        counter = 1
        if self.left is not None:
            counter += self.left.count()
        if self.right is not None:
            counter += self.right.count()
        return counter

    def get(self, key):
        if self.key == key:
            return self.value
        elif self.key > key:
            if self.left is not None:
                return self.left.get(key)
        else:
            if self.right is not None:
                return self.right.get(key)

    def max_depth(self):
        left_depth = 0
        right_depth = 0
        if self.left is not None:
            left_depth += self.left.max_depth()
        if self.right is not None:
            right_depth += self.right.max_depth()
        if left_depth > right_depth:
            return left_depth + 1
        else:
            return right_depth + 1

    def count_leafs(self):
        leaf_counter = 0
        if self.right is not None:
            leaf_counter += self.right.count_leafs()
        if self.left is not None:
            leaf_counter += self.left.count_leafs()
        if self.left is None and self.right is None:
            leaf_counter = leaf_counter + 1
        return leaf_counter

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        if self.left is not None:
            self.left.as_list(lst)
        lst.append((self.key, self.value))
        if self.right is not None:
            self.right.as_list(lst)
        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a leaf node count. That is, the number of nodes
    # with no children
    def count_leafs(self):
        if self.root is None:
            return 0
        else:
            return self.root.count_leafs()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
