import uuid

class Client():
    def __init__(self, name: str, age: int, objects: list[str], id: str = None,) -> None:
        self.id = id if id else uuid.uuid4().hex
        self.name = name
        self.age = age 
        self.objects = objects
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def get_objects(self):
        return self.objects
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'objects': self.objects
        }