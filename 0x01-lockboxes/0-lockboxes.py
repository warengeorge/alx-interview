#!/usr/bin/python3
"""
Task: Lockboxes
"""

def canUnlockAll(boxes):
    """
    Check if all boxes can be opened
    """
    # check if boxes is empty
    if len(boxes) == 0:
        return False

    unlocked = set()
    unlocked.add(0)

    for count, value in enumerate(boxes):
        # check if index box can't be unlocked
        if count not in unlocked:
            return False

        # add key indexes from unlocked box
        for key in value:
            # check each key index and update the set
            if key < len(boxes) and key > count:
                unlocked.update(boxes[key])
        unlocked.update(value)

    return True
