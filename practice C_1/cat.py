class Cat:
    def __init__(self, name, gender, age):
        self.name = name 
        self.gender = gender
        self.age = age
    
    def get_name(self):
        return self.name
    
    def get_gender(self):
        return self.gender
    
    def get_age(self):
        return self.age
    
class Dog(Cat):
    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

    def get_pet(self):
        return f'{self.name} {self.age}'

dog_1 = Dog('Max', 'boy', 7)
print(dog_1.get_pet())
    