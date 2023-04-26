#!/usr/bin/python3
"""
Task: Lockboxes
"""

def canUnlockAll(boxes):
    unlocked = [0]
    for count, value in enumerate(boxes):
        if not value:
            continue
        for key in value:
            if key < len(boxes) and key not in unlocked and key != count:
                unlocked.append(key)
    if len(unlocked) == len(boxes):
        return True
    return False
