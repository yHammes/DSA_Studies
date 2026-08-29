from idlelib import tree


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._inset_recursive(data, self.root)

    def _inset_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._inset_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._inset_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive (self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True

        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)


    def dfs_search(self, data):
        return self._dfs_search_recursive(self.root, data)

    def _dfs_search_recursive (self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True

        if self._dfs_search_recursive(node.left, data):
            return True
        if self._dfs_search_recursive(node.right, data):
            return True

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)


    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


    def post_traversal(self):
        result = []
        self._post_recursive(self.root, result)
        return result

    def _post_recursive(self, node, result):
        if node:
            self._post_recursive(node.left, result)
            self._post_recursive(node.right, result)
            result.append(node.data)

binary_tree = BinaryTree()

binary_tree.root = Node(1)
binary_tree.root.right = Node(2)
binary_tree.root.right.left = Node(3)

print(binary_tree.inorder_traversal())
