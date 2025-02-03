class TooManyStudents(Exception):
    """Exception raised when there are more than 10 students in a classroom."""
    pass


class Classroom:
    """
    Represents a classroom with a teacher, a list of students, and a course title.

    Attributes:
        teacher (Teacher): The teacher of the classroom.
        students (list): A list of students (Student objects) enrolled in the classroom.
        course_title (str): The title of the course being taught in the classroom.

    Methods:
        add_student(student): Adds a student to the classroom if the number of students is less than 10.
        remove_student(name): Removes a student from the classroom by name.
        change_teacher(new_teacher): Changes the teacher of the classroom.
    """

    def __init__(self, teacher, students, course_title):
        """
        Initializes a new Classroom instance.

        Args:
            teacher (Teacher): The teacher for the classroom.
            students (list): A list of Student objects currently in the classroom.
            course_title (str): The title of the course the classroom is holding.
        """
        self.teacher = teacher
        self.students = students
        self.course_title = course_title

    def add_student(self, student):
        """
        Adds a student to the classroom if there is space available (less than 10 students).

        Args:
            student (Student): The student to be added to the classroom.

        Raises:
            TooManyStudents: If there are already 10 students in the classroom.
        """
        if len(self.students) < 10:
            self.students.append(student)
        else:
            raise TooManyStudents

    def remove_student(self, name):
        """
        Removes a student from the classroom by their name.

        Args:
            name (str): The name of the student to remove.
        """
        for i in self.students:
            if i.name == name:
                self.students.remove(i)
                break

    def change_teacher(self, new_teacher):
        """
        Changes the teacher of the classroom.

        Args:
            new_teacher (Teacher): The new teacher to assign to the classroom.
        """
        self.teacher = new_teacher


class Person:
    """
    Represents a person with a name. This class is the base class for both Teacher and Student.

    Attributes:
        name (str): The name of the person.
    """

    def __init__(self, name):
        """
        Initializes a new Person instance.

        Args:
            name (str): The name of the person.
        """
        self.name = name


class Teacher(Person):
    """Represents a teacher, a subclass of Person."""
    pass


class Student(Person):
    """Represents a student, a subclass of Person."""
    pass
