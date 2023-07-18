class Object():
    def __init__(self, id: str, description : str, value: float) -> None:
        self.id = id
        self.description = description 
        self.value = value
    
    def get_id(self):
        return self.id

    def get_description(self):
        return self.description
    
    def get_value(self):
        return self.value