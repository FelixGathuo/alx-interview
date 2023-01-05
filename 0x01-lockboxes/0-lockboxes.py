#!/usr/bin/python3
def canUnlockAll(boxes):
    # Set of visited boxes
    visited = {0}
    # List of keys to be processed
    keys = boxes[0]
    
    while keys:
        # Take a key from the list
        key = keys.pop()
        # If the corresponding box has not been visited yet, add it to the set of visited boxes
        # and add its keys to the list of keys to be processed
        if key not in visited:
            visited.add(key)
            keys.extend(boxes[key])
    
    # Return True if all boxes (0 to n-1) have been visited, else False
    return len(visited) == len(boxes)
