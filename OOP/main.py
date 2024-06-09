from history_student import HistoryStudent
from student import Student


def main():
    student_a = Student("0123", "Bahaa")
    student_b = Student("0425", "Shibel")

    student_name = student_a.name

    print(student_name)
    print(student_b.name)

    student_a.get_help()
    student_a.other_get_help(student_b.name)

    new_his_stu = HistoryStudent("12345", "Majed")
    new_his_stu.get_help()

main()
