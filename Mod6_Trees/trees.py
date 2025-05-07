
class TreeNode:

    def __init__(self, data):
        self.payload = data
        self._left = None
        self.right = None
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



    def get_height(self):
        left_height = self.left.get_height() if self.left else 0
        right_height = self.right.get_height() if self.right else 0
        return max(left_height, right_height) + 1

        pass

    def print_tree(self):
        print(f'{self.payload} that has parent {self.parent.payload if self.parent else None}')
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

    def print_tree_in_order(self):
        if self.left:
            self.left.print_tree_in_order()
        print(f'{self.payload} that has parent {self.parent.payload if self.parent else None}')
        if self.right:
            self.right.print_tree_in_order()

    def print_tree_iter(self):
        stack = []
        stack.append(self)
        while stack:
            node = stack.pop()
            print(f'{node.payload} that has parent {node.parent.payload if node.parent else None}')
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    def print_tree_iter_bfs(self):
        queue = []
        queue.append(self)
        while queue:
            node = queue.pop(0)
            print(f'{node.payload} that has parent {node.parent.payload if node.parent else None}')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)


    def print_tree_iter_in_order(self):
        ## TODO: Not implemented yet!!
        ## DFS, In-Order
        stack = []
        stack.append(self)
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            print(f'{node.payload} that has parent {node.parent.payload if node.parent else None}')





joe = TreeNode('Joe')
jane = TreeNode('Jane')
dan = TreeNode('Dan')

joe.left = jane
jane.parent = joe
joe.right = dan

sadie = TreeNode('Sadie')
stella = TreeNode('Stella')
thomas = TreeNode('Thomas')

jane.left = sadie
jane.right = stella

dan.left = thomas

joe.print_tree()

print(f'Thomas is at height {thomas.get_height()} ')

print(f'Joe is at height {joe.get_height()} ')

print("\n\n\n")

joe.print_tree_iter_bfs()

print("\n\n\n")
joe.print_tree_in_order()


