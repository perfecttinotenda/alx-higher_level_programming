#!/usr/bin/python3
"""zvaka woma kudaro"""

def new_in_list(my_list, idx, element):

    if (idx < 0) or (idx > (len(my_list)-1)):
        return my_list

    copy = [x for x in my_list]
    copy[idx] = element
    return copy
"""Tikuramba tichi zama zama"""
