
"""
Certainly! Let's dive into **composition** in Python. 🐍

1. **What Is Composition?**
   - Composition is an **object-oriented design concept** that models a **"has-a" relationship** between classes.
   - In simpler terms, it means that **one class contains an object (or component) of another class**.
   - Imagine it like this: You have a toolbox, and inside that toolbox, you have various tools. The toolbox **"has"** those tools.

2. **How Does Composition Work?**
   - In composition, a **composite class** (let's call it `Toolbox`) **contains an instance of another class** (let's call it `Tool`).
   - The composite class **uses** the functionality provided by the component class.
   - For example:
     - Suppose we have a `Car` class that **has an engine**. The `Car` class is the composite, and the `Engine` class is the component.
     - The `Car` class delegates tasks related to the engine (like starting, stopping, and accelerating) to the `Engine` class.

3. **Why Use Composition?**
   - Composition allows you to **reuse existing code** by creating complex objects from simpler components.
   - It promotes **flexible designs** because you can easily swap out components without affecting the entire system.
   - You can **customize behavior at runtime** by changing the components.

4. **Example: Car and Engine**
   - Let's create a simple example in Python:
     ```python
     class Engine:
         def start(self):
             print("Engine started")

     class Car:
         def __init__(self):
             self.engine = Engine()

         def drive(self):
             print("Car is moving")
             self.engine.start()

     my_car = Car()
     my_car.drive()
     ```
   - Here, the `Car` class **has an instance of the `Engine` class** (composition).
   - When we call `my_car.drive()`, it prints "Car is moving" and also starts the engine.

5. **In Summary:**
   - Composition is about **combining classes** to create more complex structures.
   - It's like assembling Lego blocks: Each block (class) contributes to the final creation (composite class).

Remember, composition is a powerful tool for building modular and maintainable code. 🚀¹²

Source: Conversation with Bing, 3/11/2024
(1) Inheritance and Composition: A Python OOP Guide. https://realpython.com/inheritance-composition-python/.
(2) Composition in Python - TowardsMachineLearning. https://towardsmachinelearning.org/composition-in-python/.
(3) 10. Function Composition In Python | Advanced | python-course.eu. https://python-course.eu/advanced-python/function-composition-in-python.php.
(4) composition and aggregation in python - Stack Overflow. https://stackoverflow.com/questions/19861785/composition-and-aggregation-in-python.
(5) Inheritance and Composition in Python - GeeksforGeeks. https://www.geeksforgeeks.org/inheritance-and-composition-in-python/.
"""

class Bookshelf:
    def __init__(self, *books) -> None:
        self.books = books
    
    def __str__(self) -> str:
        return f"BookShelf with {len(self.books)} books."

class Book:
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self) -> str:
        return f"Book {self.name}"
    
book = Book("Dune")
book2 = Book("Harry Potter")
shelf = Bookshelf(book, book2)
print(shelf)