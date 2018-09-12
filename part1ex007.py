"""
Write a Python program to accept a filename from the user and print the extension of that.
"""
file_name = input("Enter file name: ")
split_file_name = file_name.split(".")
print(split_file_name[-1])
