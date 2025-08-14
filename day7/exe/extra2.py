class Dog:


    species = "Canis familiaris"

    def __init__(self, name, breed):
       
        self.name = name
        self.breed = breed

    def describe(self):
       
        return f"{self.name} is a {self.breed}. Species: {self.species}."


dog1 = Dog("Rico", "Golden Retriever")
dog2 = Dog("charlie", "Beagle")


print(dog1.describe())
print(dog2.describe())


dog1.species = "Canis lupus"


print("\nAfter modifying dog1's species:")
print(dog1.describe())  
print(dog2.describe())  
