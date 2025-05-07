class TreeNode:

    def __init__(self, data):
        self.payload = data
        self._left = None
        self._right = None
        self.parent = None

    @property
    def left(self):
        return self._left
        pass

    @left.setter
    def left(self, node):
        self._left = node
        node.parent = self

    @left.deleter
    def left(self):
        self._left.parent = None
        self._left = None

    @property
    def right(self):
        return self._right
        pass

    @right.setter
    def right(self, node):
        self._right = node
        node.parent = self

    @right.deleter
    def right(self):
        self._right.parent = None
        self._right = None

    def __str__(self):
        return f'{self.payload} that has parent {self.parent.payload if self.parent else None}'


    def insert(self, new_data):
        if new_data < self.payload:
            if not self.left:
                self.left = TreeNode(new_data)
            else:
                self.left.insert(new_data)
        else:
            if not self.right:
                self.right = TreeNode(new_data)
            else:
                self.right.insert(new_data)

    def find(self, target):
        if self.payload == target:
            return self
        if target > self.payload:
            if not self.right:
                return None
            return self.right.find(target)
        else:
            if not self.left:
                return None
            return self.left.find(target)

    def find_smallest_in_tree(self):
        if self.left:
            return self.left.find_smallest_in_tree()
        return self

    def delete_from_bst(self):
        ## Case 1: No children
        if not self.left and not self.right:
            if self.payload > self.parent.payload:
                print('Deleting right child from BST')
                del self.parent.right
            else:
                print('Deleting left child from BST')
                del self.parent.left

        ## Case 2: 1 child
        if (self.left and not self.right) or (not self.left and self.right):
            child = self.left if self.left else self.right
            if self.payload > self.parent.payload:

                self.parent.right = child
            else:

                self.parent.left = child

        ## Case 3: 2 children
        if self.left and self.right:
            successor = self.right.find_smallest_in_tree()
            self.payload = successor.payload
            del successor.parent.left



    def print_tree(self, prefix=''):
        print(f'{prefix}{self.payload} that has parent {self.parent.payload if self.parent else None}')
        if self.left:
            self.left.print_tree(prefix + '-')
        if self.right:
            self.right.print_tree(prefix + '-')

root = TreeNode(15)

root.insert(5)
root.insert(50)
root.insert(100)
root.insert(44)
root.insert(58)
root.insert(7)

root.print_tree()

print('=======\n\n')


node_to_delete = root.find(50)
print(node_to_delete)
node_to_delete.delete_from_bst()

print('=======\n\n')

root.print_tree()

smallest = root.find_smallest_in_tree()
print(smallest)