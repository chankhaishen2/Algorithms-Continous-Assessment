#references : https://www.techiedelight.com/graph-implementation-python/
class Graph:
    # Constructor for Graph
    def __init__(self, edgeList, placeList):

        # Initialize neighbourDictionary
        self.__neighbourDictionary = {}
        for place in placeList:
            self.__neighbourDictionary[place] = []

        # Set up a list of neighbouring places and distance for each place
        for (origin, destination, distance) in edgeList:
            self.__neighbourDictionary[origin].append((destination, distance))
            self.__neighbourDictionary[destination].append((origin, distance))

    def isNextToEachOther(self, place1, place2):
        """ Method to display the distance between two given places.
            Returns True if the two places are neighbours, otherwise returns False.
        """
        for (neighbour, distance) in self.__neighbourDictionary[place1]:
            if neighbour == place2:
                print(f'The distance between {place1} and {place2} is {distance}m.', end='')
                return True
        return False

    # references: https://www.geeksforgeeks.org/python-program-for-breadth-first-search-or-bfs-for-a-graph/
    def isReachableViaOtherPlace(self, place1, place2):
        """ Method to determine whether two given places are reachable via other
            places and display message to indicate the result.
            No return value.
        """

        # Performing breadth first search
        # Start from place1
        queue = [place1]
        visitedDictionary = {place1: {"Distance": 0, "Previous": None}}

        reachedPlace2 = False

        # Traverse through points in the graph
        while queue and not reachedPlace2:
            current = queue.pop(0)

            for (neighbour, distance) in self.__neighbourDictionary[current]:
                if neighbour not in visitedDictionary:
                    queue.append(neighbour)
                    distanceFromPlace1 = visitedDictionary[current]["Distance"] + distance
                    visitedDictionary[neighbour] = {"Distance": distanceFromPlace1, "Previous": current}

                    # Stop when reached place2
                    if neighbour == place2:
                        reachedPlace2 = True
                        break

        # Display message
        if reachedPlace2:
            print(f'Route from {place1} to {place2}:', end='\n')

            # Make the list of passed-by places
            passedByList = [place2]
            current = place2
            while current != place1:
                previous = visitedDictionary[current]["Previous"]
                passedByList.append(previous)
                current = previous
            passedByList.reverse()

            # Calculate distances between each place
            accumulatedDistance = 0
            for passedByPlace in passedByList:
                if passedByPlace == place1:
                    print(f'{place1}', end='')
                else:
                    nowAccumulatedDistance = visitedDictionary[passedByPlace]["Distance"]
                    distance = nowAccumulatedDistance - accumulatedDistance
                    print(f' -{distance}m-> {passedByPlace}', end='')
                    accumulatedDistance = nowAccumulatedDistance

            print(f'\nTotal distance: {accumulatedDistance}m', end='')

        else:
            print(f'Cannot find route between {place1} and {place2}.', end='')


if __name__ == "__main__":
    # Create a Graph object
    edges = [
        ["A","D",22], ["A","B",32], ["A","E",48], ["A","C",8], ["D","F",18], ["C","B",70]
    ]
    placeList = ["A","B","C","D","E","F"]
    graph = Graph(edges, placeList)

    # Ask user to input two places
    print("Places: A, B, C, D, E, F")
    print("Select any two places.")
    place1 = input("Place 1: ")
    place2 = input("Place 2: ")
    print("\nReport:")

    # Check whether the two places are next to each other
    if not graph.isNextToEachOther(place1, place2):
        # Check whether the two places is reachable via other places
        graph.isReachableViaOtherPlace(place1, place2)
