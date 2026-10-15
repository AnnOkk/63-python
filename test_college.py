from unittest import TestCase,main
from students.college import College
from students.student import Student


class TestCollege(TestCase):
    def setUp(self):
        self.college = College()

    def test_add_student(self):
        student1 = Student(1,'Alice',45)
        self.college.add_student(student1)
        self. assertIn(student1,self.college.get_all_students())

    def test_add_duplicate_student(self):
        student1 = Student(1,'Alice',45)
        self.college.add_student(student1)
        with self.assertRaises(ValueError):
            self.college.add_student(student1)
    def test_remove_student(self):
        student1 = Student(1,'Alice',45)
        self.college.add_student(student1)
        self.college.remove_student(student1)
        self.assertNotIn(student1,self.college.get_all_students())

    def test_remove_duplicate_student(self):
        student1 = Student(1,'Alice',45)
        self.college.add_student(student1)
        self.college.remove_student(student1)
        with self.assertRaises(ValueError):
            self.college.remove_student(student1)

    def test_get_all_students(self):
        student1 = Student(5,'Alice',75)
        student2 = Student(2,'Bob',15)
        student3 = Student(8,'Charlie',63)
        student4 = Student(6,'David',99)
        self.college.add_student(student1)
        self.college.add_student(student2)
        self.college.add_student(student3)
        self.college.add_student(student4)
        self.assertEqual(self.college.get_all_students(),[student2,student1,student4,student3])

    def test_get_students_by_score(self):
        student1 = Student(5, 'Alice', 35)
        student2 = Student(2, 'Bob', 5)
        student3 = Student(8, 'Charlie', 69)
        student4 = Student(6, 'David', 99)
        self.college.add_student(student1)
        self.college.add_student(student2)
        self.college.add_student(student3)
        self.college.add_student(student4)
        self.assertEqual(self.college.get_students_by_score(),[student2,student1,student3,student4])

    def test_get_student_by_id(self):
        student1 = Student(3, 'Alice', 35)
        student2 = Student(2, 'Bob', 5)
        student3 = Student(9, 'Charlie', 69)
        student4 = Student(1, 'David', 99)

        student5 = Student(6, 'David', 99)

        self.college.add_student(student1)
        self.college.add_student(student2)
        self.college.add_student(student3)
        self.college.add_student(student4)

        self.assertEqual(self.college.get_students_by_id(student1.id),student1)
        with self.assertRaises(ValueError):
            self.college.get_students_by_id(student5.id)


    def test_get_student_by_score_between(self):
        student1 = Student(3, 'Alice', 35)
        student2 = Student(2, 'Bob', 5)
        student3 = Student(9, 'Charlie', 69)

        self.college.add_student(student1)
        self.college.add_student(student2)
        self.college.add_student(student3)
        self.assertEqual(self.college.get_students_by_scores_between(3,37),[student2,student1])
        self.assertEqual(self.college.get_students_by_scores_between(80,99),[])



    def test_between_equal_scores(self):
        student1 = Student(3, 'Alice', 35)
        student2 = Student(2, 'Bob', 35)
        student3 = Student(9, 'Charlie', 35)
        self.college.add_student(student1)
        self.college.add_student(student2)
        self.college.add_student(student3)
        self.assertEqual(self.college.get_students_by_scores_between(3,37),[student1,student2,student3])

    def test_between_includes_scores(self):
        student1 = Student(8, 'Alice', 66)
        student2 = Student(2, 'Bob', 45)
        student3 = Student(11, 'Charlie', 88)
        self.college.add_student(student1)
        self.college.add_student(student2)
        self.college.add_student(student3)
        self.assertEqual(self.college.get_students_by_scores_between(45,88),[student2,student1,student3])

    def test_equal_id(self):
        student1 = Student(1, 'Alice', 45)
        student2 = Student(1, 'Bob', 55)
        self.college.add_student(student1)
        with self.assertRaises(ValueError):
            self.college.add_student(student2)

        self.assertEqual(self.college.get_all_students(), [student1])





