# First class functions just means that functions are treated as variables. 
def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be 0.")
    return dividend / divisor


def calculate(*values, operator):
    return operator(*values)

result = calculate(20,4, operator=divide)
print(result)

#  -------------------

def search(sequence, expected, finder):
    for elem in sequence:
        if finder(elem) == expected:
            return elem
    raise RuntimeError(f"Couldnt find an element with {expected}")

friends = [
    {"name": "Rolf Smith", "age": 20},
    {"name": "Jen Smith", "age": 24},
    {"name": "Jim Corn", "age": 50}
]

def get_friend_name(friend):
    return friend["name"]

print(search(friends, "Jen Smith", get_friend_name))