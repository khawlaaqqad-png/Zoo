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

class Lion(Animal):
    def __init__(self, name, health=50, happiness=50, mane_color="golden"):
        super().__init__(name, health, happiness)
        self.mane_color = mane_color

    def feed(self):
        self.health += 10
        self.happiness += 15
        return self

    def display_info(self):
        print(f"{self.name} (Lion), Mane: {self.mane_color}, Health: {self.health}, Happiness: {self.happiness}")
        return self


class Tiger(Animal):
    def __init__(self, name, health=50, happiness=50, stripes=10):
        super().__init__(name, health, happiness)
        self.stripes = stripes

    def feed(self):
        self.health += 12
        self.happiness += 10
        return self

    def display_info(self):
        print(f"{self.name} (Tiger), Stripes: {self.stripes}, Health: {self.health}, Happiness: {self.happiness}")
        return self


class Bear(Animal):
    def __init__(self, name, health=50, happiness=50, fur_color="brown"):
        super().__init__(name, health, happiness)
        self.fur_color = fur_color

    def display_info(self):
        print(f"{self.name} (Bear), Fur: {self.fur_color}, Health: {self.health}, Happiness: {self.happiness}")
        return self

class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_animal(self , animal):
        self.animals.append(animal)
        return self

    def print_all_info(self):
        print(f"{self.zoo_name}")
        for animal in self.animals:
            animal.display_info()
    
zoo1 = Zoo("My Zoo")

zoo1.add_animal(Lion("Simba"))
zoo1.add_animal(Tiger("Shebna"))
zoo1.add_animal(Bear("Baloo"))

zoo1.print_all_info()