import timeit
import random


class Node:
    def __init__(self, number):
        self.number = number
        self.leftChild = None
        self.rightChild = None


class BST:
    def __init__(self):
        self.__root = None

    def insertNumber(self, number):
        """ Method to insert a new node.
            No return value.
        """
        # Root is None
        if not self.__root:
            self.__root = Node(number)
            return

        # Root is not None
        current = self.__root
        parent = current
        while current:
            parent = current
            if current.number > number:
                current = current.leftChild
            elif current.number < number:
                current = current.rightChild
            else:
                return  # Duplicate entry
        if parent.number > number:
            parent.leftChild = Node(number)
        else:
            parent.rightChild = Node(number)

    def searchNumber(self, number):
        """ Method to search a number.
            Returns true if found, otherwise false.
        """
        current = self.__root
        while current:
            if current.number > number:
                current = current.leftChild
            elif current.number < number:
                current = current.rightChild
            else:
                return True  # Found
        return False  # Not found


# references: https://www.geeksforgeeks.org/avl-tree-set-1-insertion/
class AVL_Node:
    def __init__(self, number):
        self.number = number
        self.leftChild = None
        self.rightChild = None
        self.height = 1


class AVL:
    def __init__(self):
        self.__root = None

    def __getHeight(self, AVL_node):
        """ Method to get height of a node.
            Returns integer.
        """
        if not AVL_node:
            return 0
        return AVL_node.height

    def __leftRotate(self, AVL_node):
        """ Method to perform left rotation on a subtree.
            Returns the subtree new root.
        """
        rightChild = AVL_node.rightChild
        leftChildOfRightChild = rightChild.leftChild

        # Perform rotation
        rightChild.leftChild = AVL_node
        AVL_node.rightChild = leftChildOfRightChild

        # Update heights
        AVL_node.height = 1 + max(self.__getHeight(AVL_node.leftChild), self.__getHeight(AVL_node.rightChild))
        rightChild.height = 1 + max(self.__getHeight(rightChild.leftChild), self.__getHeight(rightChild.rightChild))

        return rightChild  # New root

    def __rightRotate(self, AVL_node):
        """ Method to perform right rotation on a subtree.
            Returns the subtree new root.
        """
        leftChild = AVL_node.leftChild
        rightChildOfLeftChild = leftChild.rightChild

        # Perform rotation
        leftChild.rightChild = AVL_node
        AVL_node.leftChild = rightChildOfLeftChild

        # Update heights
        AVL_node.height = 1 + max(self.__getHeight(AVL_node.leftChild), self.__getHeight(AVL_node.rightChild))
        leftChild.height = 1 + max(self.__getHeight(leftChild.leftChild), self.__getHeight(leftChild.rightChild))

        return leftChild  # New root

    def __insertRecursive(self, AVL_node, number):
        """ Method to insert a new node recursively.
            Returns the current node to the calling function.
        """
        # Normal BST insertion
        if not AVL_node:
            return AVL_Node(number)
        elif AVL_node.number > number:
            AVL_node.leftChild = self.__insertRecursive(AVL_node.leftChild, number)
        elif AVL_node.number < number:
            AVL_node.rightChild = self.__insertRecursive(AVL_node.rightChild, number)

        # Update the height
        AVL_node.height = 1 + max(self.__getHeight(AVL_node.leftChild), self.__getHeight(AVL_node.rightChild))

        # Get the balance factor
        balanceFactor = self.__getHeight(AVL_node.leftChild) - self.__getHeight(AVL_node.rightChild)

        # Node is balanced
        if balanceFactor in (-1, 0, 1):
            return AVL_node

        # Node is imbalance

        # Case 1: Left left imbalance
        if balanceFactor > 1 and AVL_node.leftChild.number > number:
            return self.__rightRotate(AVL_node)

        # Case 2: Right right imbalance
        if balanceFactor < -1 and AVL_node.rightChild.number < number:
            return self.__leftRotate(AVL_node)

        # Case 3: Left right imbalance
        if balanceFactor > 1 and AVL_node.leftChild.number < number:
            AVL_node.leftChild = self.__leftRotate(AVL_node.leftChild)
            return self.__rightRotate(AVL_node)

        # Case 4: Right left imbalance
        if balanceFactor < -1 and AVL_node.rightChild.number > number:
            AVL_node.rightChild = self.__rightRotate(AVL_node.rightChild)
            return self.__leftRotate(AVL_node)

    def insertNumber(self, number):
        """ Method to insert a new node.
            No return value.
        """
        self.__root = self.__insertRecursive(self.__root, number)

    def searchNumber(self, number):
        """ Method to search a number.
            Returns true if found, otherwise false.
        """
        current = self.__root
        while current:
            if current.number > number:
                current = current.leftChild
            elif current.number < number:
                current = current.rightChild
            else:
                return True  # Found
        return False  # Not found


if __name__ == "__main__":

    n = int(input("Specify number of random numbers: "))

    # Create BST/AVL
    BST_randomOrder = BST()
    BST_sorted = BST()
    AVL_randomOrder = AVL()
    AVL_sorted = AVL()

    # Prepare list of numbers
    count = 1
    numberList = []
    while count <= n:
        randomNumber = random.randint(1, 1000)
        if randomNumber not in numberList:
            numberList.append(randomNumber)
            count += 1

    # Insert numbers
    # Random order
    for num in numberList:
        BST_randomOrder.insertNumber(num)
        AVL_randomOrder.insertNumber(num)
    # Sorted
    numberList.sort()
    for num in numberList:
        BST_sorted.insertNumber(num)
        AVL_sorted.insertNumber(num)

    print("\nReport")
    print("Time used to search number 2000 for 100000 times: ")

    # references: https://www.geeksforgeeks.org/how-to-check-the-execution-time-of-python-script/
    # Search for 2000
    # BST sorted
    def execute_BST_sorted():
        BST_sorted.searchNumber(2000)
    print(f'BST sorted: {timeit.timeit(stmt=execute_BST_sorted,number=100000)}', end='\n')

    # AVL random order
    def execute_AVL_random():
        AVL_randomOrder.searchNumber(2000)
    print(f'AVL random order: {timeit.timeit(stmt=execute_AVL_random,number=100000)}', end='\n')

    # AVL sorted
    def execute_AVL_sorted():
        AVL_sorted.searchNumber(2000)
    print(f'AVL sorted: {timeit.timeit(stmt=execute_AVL_sorted,number=100000)}', end='\n')

    # BST random order
    def execute_BST_random():
        BST_randomOrder.searchNumber(2000)
    print(f'BST random order: {timeit.timeit(stmt=execute_BST_random,number=100000)}', end='\n')
