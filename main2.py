# Define the Classmate class
class Classmate:
    def __init__(self, name, section, favorite_subject):
        # Initialize attributes 
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    # Method for a uniform introduction 
    def introduce(self):
        return f"Hi! I am {self.name} from {self.section}. My favorite subject is {self.favorite_subject}."

# First 5 classmates
classmate_list = [
    Classmate("Arianne", "10 - Ruby", "English"),
    Classmate("Sophia", "10 - Emerald", "Social Studies"),
    Classmate("Dylan", "10 - Ruby", "Science"),
    Classmate("Uno", "10 - Ruby", "Math"),
    Classmate("Lesvie", "10 - Emerald", "Recess")
]

# This is the one that's gonna get operated when manually entering student data
def add_new_classmate():
    print("--- Add Classmate ---")
    name = input("Enter Name: ")
    section = input("Enter Section: ")
    subject = input("Enter Favorite Subject: ")
    
    new_student = Classmate(name, section, subject)
    classmate_list.append(new_student)
    print("Classmate added successfully!")

# Loop to display js the same introductions 
def display_all():
    print("--- Classmate List ---")
    for student in classmate_list:
        print(student.introduce())

