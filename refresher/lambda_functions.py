# lambdas are functions without a name. They are used to calculate a value
# from its parameters and arent used to perform an action.
# This add function can be rewritten as ...
def add(x, y):
    return x + y
# this lambda function
lambda x, y: x + y

# Can give lambda a name
add = lambda x, y: x + y

print(add(6,7))

# sequence = [1,3,5,9]
# doubled = [(lambda x: x * 2)(x) for x in sequence]
# doubled = list(map(lambda x: x * 2, sequence))