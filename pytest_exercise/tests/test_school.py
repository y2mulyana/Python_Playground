"""
microsoft copilot.
Using pytest and the functions that come from it. Such as fixture,
parametrize, raise and mark whenever it necessary.
Test the following code and theme it after avenger.
Import from source/school.py:
"""
# test_school.py
import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents


@pytest.fixture
def teacher_ironman():
    """
    Fixture that provides a Teacher instance with the name 'Iron Man'.
    This is used in tests where a teacher is needed.

    Returns:
        Teacher: A Teacher instance named 'Iron Man'.
    """
    return Teacher("Iron Man")


@pytest.fixture
def teacher_captain():
    """
    Fixture that provides a Teacher instance with the name 'Captain America'.
    This is used in tests where a teacher is needed.

    Returns:
        Teacher: A Teacher instance named 'Captain America'.
    """
    return Teacher("Captain America")


@pytest.fixture
def students():
    """
    Fixture that provides a list of 9 Student instances with names 'Student 1' to 'Student 9'.
    This is used in tests where a group of students is needed.

    Returns:
        list: A list of 9 Student instances.
    """
    return [Student(f"Student {i + 1}") for i in range(9)]


@pytest.fixture
def full_classroom(teacher_ironman, students):
    """
    Fixture that provides a Classroom instance with a teacher and a list of 9 students.
    This classroom is used in tests where a full classroom is needed.

    Args:
        teacher_ironman (Teacher): The teacher for the classroom.
        students (list): The list of students for the classroom.

    Returns:
        Classroom: A Classroom instance with a teacher and 9 students.
    """
    return Classroom(teacher_ironman, students, "Hero Training 101")


def test_add_student_to_not_full_classroom(full_classroom):
    """
    Test that adds a student to a not full classroom and ensures the student is added successfully.

    Args:
        full_classroom (Classroom): The full classroom to add the student to.
    """
    student_hulk = Student("Hulk")
    full_classroom.add_student(student_hulk)
    assert student_hulk in full_classroom.students


def test_add_student_to_full_classroom(full_classroom):
    """
    Test that tries to add a student to a full classroom and ensures the exception
    TooManyStudents is raised.

    Args:
        full_classroom (Classroom): The classroom that will be filled with students.
    """
    # First, fill the classroom
    full_classroom.add_student(Student("Student 10"))

    # Now, adding another student should raise the exception
    student_thor = Student("Thor")
    with pytest.raises(TooManyStudents):
        full_classroom.add_student(student_thor)


def test_remove_student(full_classroom):
    """
    Test that removes a student from the classroom and ensures the student is removed.

    Args:
        full_classroom (Classroom): The classroom from which to remove a student.
    """
    student_to_remove = full_classroom.students[0]
    full_classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in full_classroom.students


@pytest.mark.parametrize("new_teacher", [("Black Widow"), ("Hawkeye")])
def test_change_teacher(full_classroom, new_teacher):
    """
    Test that changes the teacher of the classroom and ensures the teacher is updated.

    Args:
        full_classroom (Classroom): The classroom whose teacher will be changed.
        new_teacher (str): The new teacher's name to set in the classroom.
    """
    full_classroom.change_teacher(Teacher(new_teacher))
    assert full_classroom.teacher.name == new_teacher

