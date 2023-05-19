#!/usr/bin/python3
"""Tava Task 101 Advanced"""
def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda col: col**2, row)), matrix))
