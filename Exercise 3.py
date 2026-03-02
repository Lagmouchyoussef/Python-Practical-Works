class Person:
    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
    
    def identity(self):
        print(f"Last Name: {self.last_name}, First Name: {self.first_name}, Age: {self.age} years")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.age} years old"

class Student(Person):
    def __init__(self, last_name, first_name, age, major):
        super().__init__(last_name, first_name, age)
        self.major = major
    
    def study(self):
        print(f"{self.first_name} studies in {self.major}")
    
    def __str__(self):
        return f"Student: {super().__str__()}, Major: {self.major}"

class Teacher(Person):
    def __init__(self, last_name, first_name, age, subject):
        super().__init__(last_name, first_name, age)
        self.subject = subject
    
    def teach(self):
        print(f"{self.first_name} teaches {self.subject}")
    
    def __str__(self):
        return f"Teacher: {super().__str__()}, Subject: {self.subject}"

print("\n" + "="*50)
print("EXERCISE 3 - School System")
print("="*50)

people = [
    Student("Alaoui", "Yasmine", 20, "Computer Science"),
    Student("Benali", "Omar", 22, "Mathematics"),
    Teacher("Chafik", "Fatima", 45, "Python Programming"),
    Teacher("El Fassi", "Mohammed", 52, "Database")
]

print("List of people created")

print("\nCalling identity() on each element:")
for person in people:
    person.identity()

print("\nSeparation with isinstance():")
print("\n--- Students ---")
for person in people:
    if isinstance(person, Student):
        person.study()
        print(person)

print("\n--- Teachers ---")
for person in people:
    if isinstance(person, Teacher):
        person.teach()
        print(person)
