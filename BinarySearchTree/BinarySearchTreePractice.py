class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
            return
        self.insert_children(self.root, data)
        
    def insert_children(self, current, new_val):
        if current.data < new_val:
            if current.right:
                self.insert_children(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            if current.left:
                self.insert_children(current.left, new_val)
            else:
                current.left = Node(new_val)

    def search(self, val):
        if self.root:
            if self.root.data == val:
                return True
            return self.search_children(self.root, val)
        return None
    
    def search_children(self, current, val):
        if current:
            if current.data == val:
                return True
            elif current.data < val:
                return self.search_children(current.right, val)
            else:
                return self.search_children(current.left, val)

my_bst = BST()
my_bst.insert(10)
my_bst.insert(3)
my_bst.insert(1)
my_bst.insert(25)
my_bst.insert(9)
my_bst.insert(13)
my_bst.insert(3000)
my_bst.insert(2)
my_bst.insert(350)
my_bst.insert(12)
my_bst.insert(11)
my_bst.insert(16)
my_bst.insert(351)
my_bst.insert(80)
my_bst.insert(6)
my_bst.insert(7)
my_bst.insert(4)
my_bst.insert(24)
my_bst.insert(31)
my_bst.insert(19)

print(my_bst.search(90))