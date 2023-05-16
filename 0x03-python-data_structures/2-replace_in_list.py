#!/usr/bin/python3
"""Taka yenda taka yenda"""

def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        return my_list
    else:
        my_list[idx] = element
        return my_list
"""Pusha panda play ne Python"""
