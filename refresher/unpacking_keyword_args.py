# This function will do some dictionary unpacking
# The ** collects keyword args
def named(**kwargs):
    print("in the named function")
    print(kwargs)
    
named(name="Bob", age=24)

# ----------------------
# Can unpack a dictionary as a named argument
def named2(name, age):
    print(name, age)

details = {"name": "charlie", "age": 24}
named2(**details)

# ----------------------

def print_nicely(**kwargs):
    named(**kwargs) # unpacks the dictionary
    for arg, value in kwargs.items():
        print(f'{arg}: {value}')
        
print_nicely(name="Bob", age=2567)