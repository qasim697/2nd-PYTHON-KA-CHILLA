# ccomments in python
# this is a single line comment

"""   
This is a multi-line comment
It can span multiple lines
"""
# You can also use multi-line strings as comments
# This is a comment with code
# print("This line is commented out and won't execute")

# when to use comments: 
# 1. To explain complex code
# 2. To provide context or background information
# 3. To temporarily disable code during debugging
# 4. To improve code readability for others (or yourself in the future)
# Example of using comments to explain code
def calculate_area(radius):
    # This function calculates the area of a circle given its radius
    pi = 3.14159  # Approximate value of pi
    area = pi * (radius ** 2)  # Area formula: A = πr^2
    return area
