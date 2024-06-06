#!/usr/bin/python3

'''
This module contains the function canUnlockAll(boxes) that determines
if all the boxes can be opened.
'''


def canUnlockAll(boxes):
    '''
    This function returns:
        true if all the boxes can be opened, 
        otherwise it return false.
    '''

    total_boxes = len(boxes)
    keys_collected = [0]
    open_boxes_count = 0
    index = 0

    while index < len(keys_collected):
        set_k = keys_collected[index]
        for k in boxes[set_k]:
            if 0 < k < total_boxes and k not in keys_collected:
                keys_collected.append(k)
                open_boxes_count += 1
        index += 1
    return open_boxes_count == total_boxes - 1
