class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

    def __repr__(self):
        return f"Student(name='{self.name}', roll_number='{self.roll_number}', cgpa={self.cgpa})"


def sort_students(student_list):
    """
    Sort the list of student objects based on CGPA in descending order.

    Parameters:
    student_list (list): A list of Student objects.

    Returns:
    list: A sorted list of Student objects based on CGPA in descending order.
    """
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students


# Example usage
students = [
    Student('Alice', 'A001', 3.8),
    Student('Bob', 'B002', 3.5),
    Student('Catherine', 'C003', 3.9),
    Student('David', 'D004', 3.7),
]

sorted_students = sort_students(students)

# Print the sorted list of students
for student in sorted_students:
    print(student)