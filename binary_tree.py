class Node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinaryTree():
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)  # Fixed how to set root
        else:
            self._add(self.root, value)

    def _add(self, node, value):
        if value < node.data:
            if node.left:
                self._add(node.left, value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self._add(node.right, value)  # Fixed recursive call
            else:
                node.right = Node(value)

    def search(self, val):
        return self._search(self.root, val)  # Fixed search starting point

    def _search(self, node, val):
        if node is None or node.data == val:
            return node

        if val < node.data:
            return self._search(node.left, val)

        return self._search(node.right, val)

    def findLCA(self, n1, n2):
        return self._findLCA(self.root, n1, n2)

    def _findLCA(self, node, n1, n2):
        if node is None:
            return None

        if node.data > n1 and node.data > n2:
            return self._findLCA(node.left, n1, n2)

        if node.data < n1 and node.data < n2:
            return self._findLCA(node.right, n1, n2)

        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return node

        if value < node.data:
            node.left = self._delete(node.left, value)
        elif value > node.data:
            node.right = self._delete(node.right, value)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._findMin(node.right)

            node.data = temp.data

            node.right = self._delete(node.right, temp.data)

        return node

    def _findMin(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder(self):
        def _inorder(node):
            if node is not None:
                _inorder(node.left)
                result.append(node.data)
                _inorder(node.right)

        result = []
        _inorder(self.root)
        return result


if __name__ == "__main__":
    bt = BinaryTree()
    bt.insert(20)
    bt.insert(8)
    bt.insert(22)
    bt.insert(4)
    bt.insert(12)
    bt.insert(10)
    bt.insert(14)

    print(bt.search(22).data)
    lca = bt.findLCA(10, 14)
    if lca is not None:
        print(f"Lowest Common Ancestor of 10 and 14 is: {lca.data}")
    else:
        print("Lowest Common Ancestor not found.")
    bt.delete(4)
    print("After deleting leaf node 4:", bt.inorder())
