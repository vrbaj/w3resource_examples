"""
Write a Python program to print out a set containing all the colors
 from color_list_1 which are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
Expected Output :
{'Black', 'White'}
"""


def check_color_lists(color_list_1, color_list_2):
    output = set()
    for item in color_list_1:
        if not item in color_list_2:
            output.add(item)
    return output


color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
print(check_color_lists(color_list_1, color_list_2))
