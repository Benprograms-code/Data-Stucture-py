
outputdebug = True 

def debug(msg):
    if outputdebug:
        print (msg)



class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 

    def is_leaf(self):
        return self.left is None and self.right is None


class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0)

    def insert(self, key):
        if self.node is None:
            self.node = Node(key)
            self.node.left = AVLTree()
            self.node.right = AVLTree()
        elif key < self.node.key:
            self.node.left.insert(key)
        elif key > self.node.key:
            self.node.right.insert(key)
        else:
            # Key already exists, no need for debug message
            return

        self.rebalance()

    def delete(self, key):
        if self.node is None:
            return

        if key < self.node.key:
            self.node.left.delete(key)
        elif key > self.node.key:
            self.node.right.delete(key)
        else:
            if self.node.left.node is None and self.node.right.node is None:
                self.node = None
            elif self.node.left.node is None:
                self.node = self.node.right.node
            elif self.node.right.node is None:
                self.node = self.node.left.node
            else:
                predecessor = self.logical_predecessor(self.node)
                if predecessor is not None:
                    self.node.key = predecessor.key
                    self.node.left.delete(predecessor.key)

        self.rebalance()






    def rebalance(self):
        '''
        Rebalance a particular (sub)tree
        '''
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()



    def rrotate(self):
        # Rotate left pivoting on self
        #debug ('  Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 

    
    def lrotate(self):
        # Rotate left pivoting on self
        #debug ('  Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
        
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 


    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallese valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  
        
    def inorder_traverse(self):
        if self.node == None:
            return [] 
        
        inlist = [] 
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 

        inlist.append(self.node.key)

        l = self.node.right.inorder_traverse()
        for i in l: 
            inlist.append(i) 
    
        return inlist

    
    def postorder_traverse(self):

        if self.node == None:
            return []
        
        inlist = [] 
        l = self.node.left.postorder_traverse()
        for i in l: 
            inlist.append(i) 

        

        r = self.node.right.postorder_traverse()
        for i in r: 
            inlist.append(i)

        inlist.append(self.node.key)
    
        return inlist 


    def preorder_traverse(self):
        
        if self.node == None:
            return []
        
        inlist = []
        
        inlist.append(self.node.key)

        l=self.node.left.preorder_traverse()
        
        for i in l:
            inlist.append(i)

        r=self.node.right.preorder_traverse()
        
        for i in  r:
            inlist.append(i)

        return inlist

    
    def gather_leaf_and_non_leaf_nodes(self, leaf_list=None, non_leaf_list=None):
        '''
        Gather leaf and non-leaf nodes of the tree.
        '''        
        if leaf_list is None:
            leaf_list = []
        if non_leaf_list is None:
            non_leaf_list = []

        if self.node is not None: 
            if self.node.left is not None: 
                self.node.left.gather_leaf_and_non_leaf_nodes(leaf_list, non_leaf_list)
            if self.is_leaf():
                leaf_list.append(self.node.key)
            else:
                non_leaf_list.append(self.node.key)
            if self.node.right is not None:
                self.node.right.gather_leaf_and_non_leaf_nodes(leaf_list, non_leaf_list)

        return leaf_list, non_leaf_list

    
    def display(self, level=0, pref=''):
        '''
        Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()  
        if(self.node != None): 

            if self.node.left != None: 
                self.node.left.display(level + 1, ' <')
                print ( 'key= ', self.node.key, "   height= " + str(self.height) + '    balance= ' + str(self.balance))
            if self.node.left != None:
                self.node.right.display(level + 1, ' >')














         
    def printTreeNoHB(self):            ##  https://stackoverflow.com/questions/34012886/print-binary-tree-level-by-level-in-python
        def display(root):              ##  AUTHOR: Original: J.V.     Edit: BcK
            #   No child.
            if root.node.right.node is None and root.node.left.node is None:
                line = str(root.node.key)
                width = len(line)
                height = 1
                middle = width // 2
                return [line], width, height, middle

            #   Only left child.
            if root.node.right.node is None:
                lines, n, p, x = display(root.node.left)
                nodeOutput = (str(root.node.key) )
                keyLength = len(nodeOutput)
                first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput
                second_line = x * ' ' + '/' + (n - x - 1 + keyLength) * ' '
                shifted_lines = [line + keyLength * ' ' for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, n + keyLength // 2

            #   Only right child.
            if root.node.left.node is None:
                lines, n, p, x = display(root.node.right)
                nodeOutput = str(root.node.key)
                keyLength = len(nodeOutput)
                first_line = nodeOutput + x * '_' + (n - x) * ' '
                second_line = (keyLength + x) * ' ' + '\\' + (n - x - 1) * ' '
                shifted_lines = [keyLength * ' ' + line for line in lines]
                return [first_line, second_line] + shifted_lines, n + keyLength, p + 2, keyLength // 2

            #   Two children.
            left, n, p, x = display(root.node.left)
            right, m, q, y = display(root.node.right)
            nodeOutput = str(root.node.key)
            keyLength = len(nodeOutput)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + nodeOutput + y * '_' + (m - y) * ' '
            second_line = x * ' ' + '/' + (n - x - 1 + keyLength + y) * ' ' + '\\' + (m - y - 1) * ' '
            if p < q:
                left += [n * ' '] * (q - p)
            elif q < p:
                right += [m * ' '] * (p - q)
            zipped_lines = zip(left, right)
            lines = [first_line, second_line] + [a + keyLength * ' ' + b for a, b in zipped_lines]
            return lines, n + m + keyLength, max(p, q) + 2, n + keyLength // 2

        lines = []
        if self.node != None:
            lines, *_ = display(self)
            print("\t\t== AVL Tree ==")
            print()
        if lines == []:
            print("No tree found, please rebuild a new Tree.\n")
            return -1
        for line in lines:
            print(line)
        print()     



















def menu_lvl_2(inlist1):
    while True:
        print('1. display AVL tree showing height and balance factor for each node')
        print('2. print the pre-order, in-order, and post-order traversal sequences for the AVL tree')
        print('3. print all leaf nodes, and all none leaf nodes seperately')
        print('4. insert new key integer into the AVL tree')
        print('5. delete a node from the AVL tree')
        print('6. return to level-1 menu')
        b = AVLTree(inlist1)


        user_input=int(input('choose your option: '))

        if user_input==1:


            b.display()
            b.printTreeNoHB()






        elif user_input==2:


            print('\npre order traverse: ', b.preorder_traverse(),'\n')
            print('in order traverse: ', b.inorder_traverse(), '\n')
            print('post order traverse: ', b.postorder_traverse(),'\n')




        elif user_input==3:




            leaf_nodes, non_leaf_nodes= b.gather_leaf_and_non_leaf_nodes()
            print ('\n','leaf nodes are: ',leaf_nodes,'\n')
            print('leaf nodes are: ', non_leaf_nodes, '\n')




        elif user_input==4:



             user_input=int(input('enter a value to add to the AVL tree: ' ))
             if user_input in inlist1:
                print("that number already exist")
             else:


                b.insert(user_input)
             ## inserts the value but need to rebalance the sub trees



                b.printTreeNoHB()









        elif user_input==5:

            b.printTreeNoHB()


            user_input=int(input('enter value you would like to delete: '))
            if user_input not in inlist1:
                print("value doesn't exist")
            else:
                b.delete(user_input)

                b.printTreeNoHB()






        elif user_input==6:
            break

        else:

            print('invalid input')
            pass



def menu_lvl_1():
    inlist1 = []

    while True:
        
        print('1. Pre-load a sequence of integers to build an AVL tree')
        print('2. manually enter integer keys to build an AVL tree')
        print('3.exit')
        
        user_input=int( input('choose an option: ' ))

        if user_input==1:
            
            a = AVLTree()
            print ("----- Inserting:\n")
            inlist1 = [9,-1,45,6,8,21,34,5,55,65,543,18,90,122,132,0,66,100,-12,17]
           
            
            menu_lvl_2(inlist1)
            
        elif user_input==2:
            
            a = AVLTree()
            inlist1 = []
            try:
            
                while True:
                    user_input=int(input('enter an integer key (press any key to exit): '))
                    inlist1.append(user_input)
                
            except ValueError:
                print("test")


            

            
        else:
            break

menu_lvl_1()
