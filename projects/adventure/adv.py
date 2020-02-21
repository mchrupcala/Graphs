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
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
        if r1 in self.room_graph and self.room_graph[r1] == {}:
            self.room_graph[r1] = {'n': '?', 's': '?','w': '?','e': '?'}
        elif r1 in self.room_graph:
            pass
        else:
            raise IndexError("That room/direction does not exist!")

    def get_rooms(self, room_id):
        # return player.current_room.get_exits()
        return room_id.get_exits()


# def populate_graph(self):
#     self.room_graph.add_directions()

# The problem right now is...I can't store directions in Stack b/c they'll be useless when I move rooms.

    def dft(self, starting_room):
        s = Stack()
        s.push([starting_room])
        # Create an empty set to store visited nodes
        # visited_in_stack = {}
        # if starting_room.id not in visited_rooms:
        #     visited_rooms.add(starting_room.id)

        while s.size() > 0:
            #Normally I'd pop this off...but I don't WANT to, UNLESS no room directions left to explore
            path = s.stack[-1]
            starting_room = path[-1]
            #if room hasn't been visited, create an array in visited_in_stack & explore.
            #but if room HAS been visited, but still directions to explore, then explore anyway, just don't write a new array.
            if starting_room.id not in self.room_graph:
                self.add_room(starting_room.id)
                self.add_directions(starting_room.id, self.get_rooms(starting_room))

            # If there are rooms to explore, start exploring!
            while starting_room.id not in self.room_graph or '?' in list(self.room_graph[player.current_room.id].values()):

                #Maybe somthing like...if '?' in room direction, add neighbors to stack? then move in that direction, add direction to traversal_path, add new room to visited_in_stack, rinse repeat.
                # Then push all neighbors to the top of the stack
                cur_room_map = self.room_graph[player.current_room.id]
                starting_room = player.current_room
                # print("I'm stuck in room ", player.current_room.id)
                if '?' in list(cur_room_map.values()):
                    direction = ''
                    for i in cur_room_map:
                        if cur_room_map[i] == '?':
                            direction = i
                            break
                        else:
                            pass
                    # direction = i
                    opposite_direction = ''
                    if direction == 'n':
                        opposite_direction = 's'
                    elif direction == 's':
                        opposite_direction = 'n'
                    elif direction == 'e':
                        opposite_direction = 'w'
                    else:
                        opposite_direction = 'e'
                    # print(i)
                    player.travel(i)
                    if player.current_room.id != starting_room.id:
                        print("Travelled to ", player.current_room.id)

                        new_path = [*path, player.current_room]
                        print(new_path)
                        # add path to stack
                        s.push(new_path)
                        # add direction in both rooms to room_graph
                        self.add_room(player.current_room.id)
                        self.add_directions(player.current_room.id, self.get_rooms(player.current_room))
                        self.room_graph[starting_room.id][direction] = player.current_room.id
                        self.room_graph[player.current_room.id][opposite_direction] = starting_room.id
                        # self.room_graph[player.current_room.id]['s'] = cur_room.id
                        # add direction to traversal_path
                        traversal_path.append(direction)
                        # add room to visited_in_stack()
                        # visited_in_stack[cur_room.id].append('n')
                        # visited_rooms.add(player.current_room.id)
                    else:
                        # add 'X' to room_graph for cur_room in 'n'
                        cur_room_map[direction] = 'X'
                        # print(self.room_graph)
            s.pop()
            if len(s.stack) != 0:
                new_path = s.stack[-1]
                new_starting_room = new_path[-1]
                print("Visted rooms: ", len(visited_rooms), 'room graph: ', len(self.room_graph))
                for direction, room in self.room_graph[player.current_room.id].items():
                    if room == new_starting_room.id:
                        player.travel(direction)
                        traversal_path.append(direction)







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
print("visited rooms: ", visited_rooms)
print(room_graph)
print(len(room_graph))

# visited_rooms.add(player.current_room)
#######################################################



### player moves to my selected/traversed paths & adds any rooms to visited_rooms
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)


print("CHECK IT")
print(len(visited_rooms))
print(visited_rooms)
print(len(room_graph))
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
