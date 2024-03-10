class ClassTest:
    # this type of method is to produce an action 
    def instance_method(self):
        print(f"Called instance_method of {self}")
    
    @classmethod
    # would use this type of method as a factory
    def class_method(cls):
        print(f"Called class_method of {cls}")
    
    @staticmethod
    def static_method():
        print("Called static_method.")
        
ClassTest.static_method()