#!/usr/bin/python3

# Create a queue to store the keys that need to be checked
queue = [0]

# While there are keys in the queue
while queue:
    # Get the key from the queue
    key = queue.pop(0)
    # For each box in the list of boxes
    for box in boxes:
        # If the key is present in the box
        if key in box:
            # Add the box to the set of openable boxes
            openable_boxes.add(boxes.index(box))
            # Add the keys in the box to the queue
            queue += box

# If the number of openable boxes is equal to the total number of boxes
if len(openable_boxes) == len(boxes):
    # All boxes are openable
    return True
# If the number of openable boxes is less than the total number of boxes
else:
    # Some boxes are not openable
    return False
