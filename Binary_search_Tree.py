class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, data):
    if root is None:
        return Node(data)
    else:
        if root.key == data:
            return root
        elif root.key < data:
            root.right = insert(root.right, data)
        else:
            root.left = insert(root.left, data)
    return root


def succesor(root):
    temp = root
    while temp.left is not None:
        temp = temp.left
    return temp


def delete(root, data):
    if root.key < data:
        root.right = delete(root.right, data)
    elif root.key > data:
        root.left = delete(root.left, data)
    else:
        if root.left is None:
            temp = root.right
            del root
            return temp
        if root.right is None:
            temp = root.left
            del root
            return temp
        temp = succesor(root.right)
        root.key = temp.key
        root.right = delete(root.right, temp.key)
    return root


def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.key, end=" ")
    inorder(root.right)


if __name__ == '__main__':
    root = Node(10)
    insert(root, 5)
    insert(root, 20)
    insert(root, 2)
    inorder(root)
    print("\n")
    delete(root,10)
    inorder(root)
