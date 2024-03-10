"""
The star (*) is saying that we're going to collect a bunch of arguments
into a tuple of arguments
"""
def multiply(*args):
    print(args)
    total = 1
    for arg in args:
        total = total * arg
    return total

print(multiply(1,3,5))

# -------------------------

# Can also use the * to destructure parameters
def add(x, y):
    return x + y
nums = [3, 5]
print(add(*nums)) # the args in nums gets deconstructed into x, y params

nums2 = {"x": 15, "y" : 10}
print("With dictionaries: ", add(nums2["x"], nums2["y"]))
print("With dictionaries 1: ", add(x=nums2["x"], y=nums2["y"]))
print(add(**nums2))

# -------------------------

# The bug: Why does using * return a tuple instead of multiplying each value in it?
def apply(*args, operator):
    if operator == "*":
        # I passed in a tuple here. It needs to be *args
        return multiply(*args)
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()"

print("Apply function output: ",apply(1,3,5, 7, operator="+"))