class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __str__(self):
        return f"{self.name} (Roll Number: {self.roll_number}, CGPA: {self.cgpa})"

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("arun", "101", 3.9),
    Student("Boby", "102", 3.7),
    Student("Char", "103", 3.8),
    Student("Davi", "104", 3.95),
]

sorted_students = sort_students(students)
print("Sorted Students:")
for student in sorted_students:
    print(student)
