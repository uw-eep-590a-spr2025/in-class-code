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

    def print_tree(self):
        print(f'{self.payload} that has parent {self.parent.payload if self.parent else None}')
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()


class LinkListNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def make_lists(root):
    output = []

    queue = []

    queue.append(root)

    while True: ## Iterating through all the levels
        cur_list = []
        child_queue = []
        while queue: ## Iterating through a single level

            node = queue.pop(0)
            print(node.payload)
            cur_list.append(node.payload)
            if node.left:
                child_queue.append(node.left)
            if node.right:
                child_queue.append(node.right)

        print(cur_list)

        output.append(cur_list)
        if not child_queue:
            break
        queue = child_queue


    return output





root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)


# root.print_tree()

response = make_lists(root)

print(response)