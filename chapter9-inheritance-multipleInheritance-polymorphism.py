#class example
class Person:
    def __init__(self, firstname, lastname, health, status):
        " initialize attributes to be used in/available for all \
        class methods in this class, and for class objects created \
        by this class."

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        "All people introduce themselves"
        print("Hello, my name is {} {}".format(self.firstname, self.lastname))

    def status_change(self):
        if self.health == 100:
            print("{} is totally healthy!".format(self.firstname))
        elif self.health >=76:
            print("{} is a little tired today.".format(self.firstname))
        elif self.health >= 51:
            print("{} feels unwell.".format(self.firstname))
        elif self.health >= 40:
            print("{} goes to the doctor".format(self.firstname))
        else:
            print("{} is unconscious.".format(self.firstname))

Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print("{} is my friend? {}".format(Maria.firstname, Maria.status))
print("{} is my friend? {}".format(Rey.firstname, Rey.status))

Maria.introduce()
Rey.introduce()


#inheritance example
class Enemy(Person):
    def __init__(self, weapon, firstname, lastname, health, status):
        super().__init__(firstname, lastname, health, status)
        self.weapon = weapon

    def introduce(self):
        print("You are my mortal enemy!!!")

    def hurt(self, other):
        if self.weapon == 'rock':
            other.health -= 10
        elif self.weapon == 'stick':
            other.health -= 5
        print(other.health)

    def insult(self, other):
        if other.health <= 80:
            print("{}, you are tired and weak".format(other.firstname))

    def steal(self, other):
        print("ha ha ha, {}, I have your stuff!".format(other.firstname))
        if other.status == True:
            other.status = False

Alex = Enemy('rock', 'Alex', 'Wayne', 75, status = False)
Alex.hurt(Maria)
Alex.insult(Rey)
Alex.insult(Lee)
Alex.steal(Rey)

# error condition
Rey.steal(Alex)

# Multiple inheritance
# Parent class 1
class Item():
    def __init__(self, sku):
        self.sku = sku

    def print_sku(self):
        print("The sku is {}.".format(self.sku))

# Parent class 2
class Garment():
    def __init__(self, section, type):
        self.section = section
        self.type = type

    def print_garment(self):
        print("The garment is in section {}, {}.".format(self.section, self.type))

# Child Class
class Shirts(Item, Garment):
    def __init__(self, sku, section, type, name, color):
        self.name = name
        self.color = color
        Item.__init__(self, sku)
        Garment.__init__(self, section, type)

    def print_shirt(self):
        print("{} {} on sale!".format(self.color, self.name))

Blouse = Shirts("00001", 43, "Tops", "Formal Blouse", "White")

Blouse.print_sku()
Blouse.print_garment()
Blouse.print_shirt()