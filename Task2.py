class Student:
    def __init__(self, age, address, mark):
        self.age = age
        self.address = address
        self.mark = mark

    def __str__(self) -> str:
        return "age: " + str(self.age) + ", address: " + str(self.address) + ", mark: " + str(self.mark)


def get_students() -> dict:
    return {
        "Petrov": Student(15, "adress1", 5),
        "Dimov": Student(16, "adress2", 1),
        "Artemov": Student(17, "adress3", 8),
        "Svetava": Student(17, "adress4", 9),
        "Olynia": Student(18, "adress5", 3)
    }


def print_student_with_highest_mark():
    max_mark = 0
    max_key = -1
    for key, value in students.items():
        if value.mark > max_mark:
            max_mark = value.mark
            max_key = key
    print("Student with highest mark: " + str(students[max_key]))


if __name__ == '__main__':
    students = get_students()
    print_student_with_highest_mark()

    avg = 0
    for key, value in students.items():
        avg += value.mark
    print("Average mark: " + str(avg / len(students)))