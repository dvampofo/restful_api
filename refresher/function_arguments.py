def say_hello(name, surname):
    print(f'Hello {name} {surname}')
    
say_hello("Jim", "Jones")

# positional arguments must come first before keyword arguments
say_hello(surname="Jones", name="James")