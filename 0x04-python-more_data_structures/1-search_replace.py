#!/usr/bin/python3
"""Bo hwre pano"""
def search_replace(my_list, search, replace):
    return [replace if search == n else n for n in my_list]
