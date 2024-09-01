class Cat:
    def __init__(self, name):
        self.name = name

class Dog(Cat):
    def __init__(self, name, gender, age):
        super().__init__(name)
        self.gender = gender
        self.age = age

    def get_pet(self):
        return f'{self.name} {self.age}'
    
class Customer:
    def __init__(self, name, last_name, city, balance):
        self.name = name
        self.last_name = last_name
        self.city = city
        self.balance = balance
    
    def __str__(self):
        return f'{self.name} {self.last_name}. {self.city}. Баланс: {self.balance} руб.'
    
    def get_customer(self):
        return self.name, self.last_name, self.city

dog_1 = Dog("Felix", "boy", 2)
customer_1 = Customer('Иван', 'Петров', 'Москва', 50)
customer_2 = Customer('Денис', 'Шемонаев', 'Бийск', 0)
customer_3 = Customer('Алексей', 'Федоров', 'Барнаул', 420)

customers = [customer_1, customer_2, customer_3]
for client in customers:
    print(client.get_customer())