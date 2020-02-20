from room import Room
from player import Player
from world import World
from util import Stack, Queue

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.room_graph = {}

    def add_room(self, room_id):
        """
        Add a room to the graph.
        """
        if room_id in self.room_graph:
            print("WARNING: That room already exists")
        else:
            self.room_graph[room_id] = {}

    def add_directions(self, r1, directions):
        """
        Add a directed edge to the graph.
        """
        print("R1: ", r1, "Directions: ", directions)
        print(self.room_graph)
        if r1 in self.room_graph:
            self.room_graph[r1] = directions
        else:
            raise IndexError("That room/direction does not exist!")

    def get_rooms(self, room_id):
        # return player.current_room.get_exits()
        return room_id.get_exits()


# def populate_graph(self):
#     self.room_graph.add_directions()

# The problem right now is...I can't store directions in Stack b/c they'll be useless when I move rooms.

    def dft(self, starting_room):
        # Create an empty stack
        s = Stack()
        # Push the starting vertex_id to the stack
        s.push(starting_room)
        # Create an empty set to store visited nodes
        # line 70
        # While the stack is not empty...
        while s.size() > 0:
            # Pop the first room
            cur_room = s.pop()
            # Check if it's been visited
            # If it has not been visited...
            if cur_room.id not in visited_rooms:
                # Mark it as visited
                print(cur_room)
                visited_rooms.add(cur_room.id)
                self.add_room(cur_room)
                self.add_directions(cur_room, self.get_rooms(cur_room))
                # Then push all neighbors to the top of the stack
                # for room in self.get_rooms(cur_room):
                #     print(room)
                #     s.push(room)



# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

g = Graph()



# I need get_exits()...it returns the room directons from the currrent room
# when I have those directions...depending on which room I'm in, only explore the ones I haven't visited yet.


################### TRAVERSAL TEST ###################
visited_rooms = set()
player.current_room = world.starting_room
print("Current room: ", player.current_room.id)
# Call dft(), pass in starting room.
g.dft(player.current_room)

# visited_rooms.add(player.current_room)
#######################################################



### player moves to my selected/traversed paths & adds any rooms to visited_rooms
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)




if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
