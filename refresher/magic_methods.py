class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    # Use when you want to return the obj as a string like printing out
    def __str__(self) -> str:
        return f"Person {self.name} is {self.age} years old"
    
    # Use when you want to recreate an unambiguous representation of an obj
    def __repr__(self) -> str:
        return f"<Person({self.name}, {self.age})>"
    
    
jim = Person("jim", 23)
print(jim)