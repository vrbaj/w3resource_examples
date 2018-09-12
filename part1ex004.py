"""
Write a Python program which accepts the radius of a circle from the user and compute the area. Go to the editor
Sample Output :
r = 1.1
Area = 3.8013271108436504
"""
import math

PI = math.pi
radius = input()
try:
    radius = float(radius)
    print("r = ", radius)
    print("Area = ", PI * radius ** 2)
except Exception as ex:
    print("Exception occurred", ex)
