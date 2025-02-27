class Person:
    def __init__(self, name, age,address,gender):
        self.name = name          
        self.__age = age 
        self.gender = gender    
        self.address = address     
    
    def get_age(self):
        return self.__age
    def set_age(self, age,):
        if age >= 0:
            self.__age = age


  
    def display(self):
        print(f"Name: {self.name}, Age: {self.get_age()} Gender: {self.gender} Address:{self.address}")

person = Person("Herminio LLoveras", 22, "male ", "baragay No Level")

print(person.name)  
print(person.get_age())  
person.set_age(35)  
person.set_age(-5) 
print(person.gender) 
print(person.address)
