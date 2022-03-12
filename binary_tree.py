COUNT = [10]

class BinaryTree():
    def __init__(self, value):
        #self.root = self
        self.value = value
        self.right = None
        self.left = None
        self.hd = 0

    def __str__(self):
        return self.value

    def traverse_preorder(self, node):
        if node:
            print( '-> ', node.value, end='')
            self.traverse_preorder(node.left)
            self.traverse_preorder(node.right)

    def traverse_postorder(self, node):
        if node:
            self.traverse_postorder(node.left)
            self.traverse_postorder(node.right)
            print( '-> ', node.value, end='')

    def traverse_inorder(self, node):
        if node:
            self.traverse_inorder(node.left)
            print( '-> ', node.value, end='')
            self.traverse_inorder(node.right)
            
    def reverse_tree(self, node):
        if node:
            right = node.left
            left = node.right
            node.left = left
            node.right = right

            self.reverse_tree(node.right)
            self.reverse_tree(node.left) 
            
        return node

    def fillMap(self, root, d, l, m):
        if(root == None):
            return
 
        if d not in m:
            m[d] = [root.value, l]
        elif(m[d][1] > l):
            m[d] = [root.value, l]
        self.fillMap(root.left, d - 1, l + 1, m)
        self.fillMap(root.right, d + 1, l + 1, m)
 
    # function should print the topView of
    # the binary tree
 
 
    def topView(self, root):
 
        # map to store the pair of node value and its level
        # with respect to the vertical distance from root.
        m = {}
 
        self.fillMap(root, 0, 0, m)
        for it in sorted(m.keys()):
            print(m[it][0], end=" ")


    # function should print the topView
    # of the binary tree
 
 
    def top_view(self, root):
 
        if(root == None):
            return
        q = []
        m = dict()
        hd = 0
        root.hd = hd
 
        # push node and horizontal
        # distance to queue
        q.append(root)
 
        while(len(q)):
            root = q[0]
            hd = root.hd
 
            # count function returns 1 if the
            # container contains an element
            # whose key is equivalent to hd,
            # or returns zero otherwise.
            if hd not in m:
                m[hd] = root.value
            if(root.left):
                root.left.hd = hd - 1
                q.append(root.left)
 
            if(root.right):
                root.right.hd = hd + 1
                q.append(root.right)
 
            q.pop(0)
        for i in sorted(m):
            print(m[i], end="")

    # Function to print binary tree in 2D
    # It does reverse inorder traversal
    def print2DUtil(self, root, space) :
 
        # Base case
        if (root == None) :
            return
 
        # Increase distance between levels
        space += COUNT[0]
 
        # Process right child first
        self.print2DUtil(root.right, space)
 
        # Print current node after space
        # count
        print()
        for i in range(COUNT[0], space):
            print(end = " ")
        print(root.value)
 
        # Process left child
        self.print2DUtil(root.left, space)
 
    # Wrapper over print2DUtil()
    def print2D(self, root) :
     
    # space=[0]
    # Pass initial space count as 0
        self.print2DUtil(root, 0)

p = BinaryTree('P')
i = BinaryTree('I')
l = BinaryTree('L')
a = BinaryTree('A')
r = BinaryTree('R')
r2 = BinaryTree('R')
r3 = BinaryTree('R')
r5 = BinaryTree('R')
r4 = BinaryTree('R')
p.left = i
i.left = l
i.right = a
p.right = r

#print(p)
p.traverse_preorder(p)
print("\n-------------")
p.traverse_postorder(p)
print("\n-------------")
p.traverse_inorder(p)
print("\n-------------")
#p.reverse_tree(p)

#p.traverse_preorder(p)

# print(p.left, p.right.left, p.right.right)
p.print2D(p)


p.reverse_tree(p)
p.print2D(p)