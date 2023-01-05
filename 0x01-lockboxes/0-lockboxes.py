#!/usr/bin/python3
def canUnlockAll(boxes):
"""
This function takes a list of lists as input, where each list represents a box.
The boxes are numbered from 0 to n-1. Each box may contain keys to the other boxes.
A key with the same number as a box opens that box. The function returns True if all
boxes can be opened, else False.
"""
# We create a set to store the boxes that are opened
opened = set()
# We start by adding the first box to the set
opened.add(0)
# We create a queue to store the keys that we find
queue = boxes[0]
# While the queue is not empty, we continue searching for keys
while queue:
# We take the first element in the queue
key = queue.pop(0)
# If the key is a box that has not been opened yet, we add it to the opened set and
# add its keys to the queue
if key not in opened:
opened.add(key)
queue += boxes[key]
# If the number of opened boxes is equal to the total number of boxes, we return True
# Else, we return False
return len(opened) == len(boxes)
