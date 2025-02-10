class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def open_door(self):
        if self.age >= 3:
            return True
        else:
            return False