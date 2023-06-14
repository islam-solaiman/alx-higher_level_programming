#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        new.append([j*j for j in i])
    return new
