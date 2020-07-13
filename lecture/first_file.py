command = input
# if command in ['n', 's', 'e', 'w']:
commands = ['n', 's', 'e', 'w', 'q', 'p', 'i', 'l', 'm']
commands[1]  # Constant time operation.
# Does not depend on the size of the list. 
# Could be index 0 or index 10000. Same amount of time for both.

# accessing a dictionary value by key
rooms = {'outside': Room(...), ....}
rooms['outside']  # same as doing an index for a list. 


# Linear time op
# depends on the number of elements in the commands list.
for command in commands:
    #do something
    
    for key, value in rooms.items(): # linear time op. You touch every item in the dictionary.

# print out every combination of pairs of commands from our command list
for x in commands: # 9 commands
    for y in commands: # 9 commands
        print(x, y) # will return 81 prints
        # (n, n), (n, s), (n, e), ....
        # (s, n), (s, s), (s, e), ....