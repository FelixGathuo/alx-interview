def canUnlockAll(boxes):
    '''
    This function takes a list of boxes as input, where each box is a list of keys.
    The function returns True if all the boxes can be opened, else it returns False.
    '''
    # Initialize a set of keys that are available
    keys = set()

    # Add the keys in the first box to the set of keys
    keys.update(boxes[0])

    # Initialize a set of boxes that have been opened
    opened_boxes = {0}

    #  While there are keys available and not all boxes have been opened,
    while keys and len(opened_boxes) < len(boxes):
    
        # Take a key from the set
        key = keys.pop()
    
        # If the key is a valid box number and the box has not been opened yet,
        if key < len(boxes) and key not in opened_boxes:
        
            # Add the key to the set of opened boxes
            opened_boxes.add(key)
        
            # Add the keys in the box to the set of keys
            keys.update(boxes[key])

    # Return True if all boxes have been opened, else return False
    return len(opened_boxes) == len(boxes)
