class HashNode:
    def __init__(self, id, description):
        self.id = id
        self.description = description

class HashTable:
    def __init__(self, maxsize):
        self.__MAXSIZE = maxsize
        self.__hashTable = []
        self.__hashTable = [[] for _ in range(maxsize)]

    def __hashing(self, id):
        """ Method to convert the id to a hash value.
            Returns integer.
        """
        return id % self.__MAXSIZE  # 7 11

    def insertTask(self, id, description):
        """ Method to insert task into index given and display appropriate message.
            No return value.
        """
        index = self.__hashing(id)
        for hashNode in self.__hashTable[index]:
            if hashNode.id == id:
                print("Duplicate task id.")
                return
        self.__hashTable[index].append(HashNode(id, description))
        print("Task is inserted.")

    def retrieveTask(self, id):
        """ Method to display task description based on id.
            No return value.
        """
        index = self.__hashing(id)
        for hashNode in self.__hashTable[index]:
            if hashNode.id == id:
                print(f'Task is: {hashNode.description}', end='\n')
                return
        print("Task is not found.")

    def displayHashTable(self):
        """ Method to display the hash table.
            No return value. """
        for index in range(len(self.__hashTable)):
            print(f'Table[{index}]', end='')
            for hashNode in self.__hashTable[index]:
                print(f'-->{hashNode.id}({hashNode.description})', end='')
            print()  # Next line


if __name__ == "__main__":
    hashTable = HashTable(7)

    print("1) Add a new task")
    print("2) Retrieve a task")
    print("3) Exit")

    while True:

        option = input("\nChoose an option: ")

        # Add task
        if option == "1":
            id = int(input("Task id: "))
            description = input("Task description: ")
            hashTable.insertTask(id, description)

        # Retrieve task
        elif option == "2":
            id = int(input("Task id: "))
            hashTable.retrieveTask(id)

        # Exit
        elif option == "3":
            print("\nSummary:")
            hashTable.displayHashTable()
            break
