#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return (list(map(lambda c: list(map(lambda f: f**2, c)), matrix)))
