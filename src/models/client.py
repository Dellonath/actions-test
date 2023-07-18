class Client():
    def __init__(self, name : str, age: int, objects: list[str]) -> None:
        self.name = name
        self.age = age 
        self.objects = objects
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_objects(self):
        return self.objects