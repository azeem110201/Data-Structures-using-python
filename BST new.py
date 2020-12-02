class Node(object):
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self,key):
        newNode = Node(key)
        if self.root == None:
            self.root = newNode

        else:
            curr_node = self.root

            while True:
                if key < curr_node.data:
                    if curr_node.left == None:
                        curr_node.left = newNode
                        break
                    else:
                        curr_node = curr_node.left

                elif key > curr_node.data:
                    if curr_node.right == None:
                        curr_node.right = newNode
                        break
                    else:
                        curr_node = curr_node.right

                else:
                    pass

    def preorder(self,curr_node):
        if curr_node:
            print(curr_node.data,end=" ")
            self.preorder(curr_node.left)
            self.preorder(curr_node.right)

    def inorder(self,curr_node):
        if curr_node:
            self.inorder(curr_node.left)
            print(curr_node.data,end=" ")
            self.inorder(curr_node.right) 

    def postorder(self,curr_node):
        if curr_node:
            self.postorder(curr_node.left)
            self.postorder(curr_node.right)
            print(curr_node.data,end=" ")


            


bst = BST()
bst.insert(30)
bst.insert(10)
bst.insert(40)
bst.insert(5)
bst.insert(20)
bst.insert(50)

#https://github.com/siddhesh10/Binary_Search_Tree/blob/master/binary_search_tree.py

bst.preorder(bst.root)
print()
print('----------------')
bst.inorder(bst.root)
print()
print('----------------')
bst.postorder(bst.root)
