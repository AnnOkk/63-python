from sortedcontainers import SortedSet, SortedKeyList

from students.student import Student


class College:
    def __init__(self):
        self._students = SortedSet()
        self._students_by_score = SortedKeyList(key=lambda s: s.score) ##are we need id?

    def add_student(self, student):

        if student in self._students:
            raise ValueError(f"Student {student} already exists")
        self._students.add(student)
        self._students_by_score.add(student)


    def remove_student(self, student):
        if student not in self._students:
            raise ValueError(f"Student {student} does not exist")
        self._students.remove(student)
        self._students_by_score.remove(student)

    def get_all_students(self):
        return list(self._students)

    def get_students_by_score(self):
        return list(self._students_by_score)

    def get_students_by_scores_between(self,min_score,max_score):
        #todo homework include min and max
        res = self._students_by_score.irange_key(min_score,max_score,inclusive=(True,True))
        return list(res)






    def get_students_by_id(self,student_id): #Сам факт, что _students отсортирован по id, не означает, что метод автоматически знает, какого студента нужно найти.
        student = Student(student_id, "", 0)
        index = self._students.bisect_left(student)
        ss_id=self._students[student_id]
        if index>=len(self._students):
            raise ValueError(f"Student {ss_id} does not exist")
        if self._students[index] == student:
            return self._students[index]
        raise ValueError(f"Student {ss_id} does not exist")







