"""
Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
"""
from math import sqrt


def euclidean_distance(point1, point2):
    distance = 0
    if len(point1) == len(point2):
        for coordinate1, coordinate2 in zip(point1, point2):
            distance = distance + (coordinate1 - coordinate2) ** 2
        distance = sqrt(distance)
        return distance
    else:
        return "vectors must be same dimension"


print(euclidean_distance([1, 3], [0, 0]))
