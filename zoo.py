class Animal :
    def __init__(self , Animal_name ,health ,happiness ):
        self.name = Animal_name
        self.health = health
        self.happiness = happiness

#دالة طباعة معلومات الحيوان 
    def display_info(self):
        print(f"{self.name} , {self.health} , {self.happiness}")
        return self
#دالة اطعام حيوان
    def feed(self):
        self.health +=10
        self.happiness +=10
        return self

Wolf = Animal("Wolf" , 85 , 65)

Wolf.display_info()
Wolf.feed()
print(Wolf.happiness)

class carnivorous_animal(Animal):
    def __init__(self , color ,Animal_name, health ,happiness ):
        super().__init__(Animal_name ,health ,happiness)
        self.color = color

    def feed(self):
        self.health += 10
        self.happiness += 15
        return self 
    
    def display_info(self):
        print(f"{self.color}, {self.name}, {self.health}, {self.happiness},")
        return self
        
Lion = carnivorous_animal("orange","Lion", 50 , 40)
Lion.feed()
Lion.display_info()

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self , animal):
        self.animals.append(animal)
        return self
    
my_zoo = Zoo("my_zoo")
my_zoo.add_animal(Wolf).add_animal(Lion)

#لطباعة معلومات الحيوانات داخل zoo
for animal in my_zoo.animals:
    animal.display_info()