#!/usr/bin/python3
def islower(c):
    """Check for lowercase char"""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False
