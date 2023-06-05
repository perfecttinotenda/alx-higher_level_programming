#!/usr/bin/python3
"""Task-101"""

def safe_function(fct, *args):
    import sys
    try:
        result = fct(*args)
        return result
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return None
"""End"""
