class School:
  def __init__(self, name, foundation_year):
    self.name=name
    self.foundation_year=foundation_year
    self.students=[]
    self.teachers=[]

    def add_new_student(self, student_name, student_class):
        new_student = {'name': student_name,'class': student_class}
        self.students.append(new_student)

    def add_new_teacher(self, teacher_name, teacher_branch):
        new_teacher={"name": teacher_name, "branch": teacher_branch}
        self.teachers.append(new_teacher)

    def view_student_list(self):
        for i in self.students:
            print(f"Name: {i['name']}, Class: {i['class']}")

    def view_teacher_list(self):
        for i in self.teachers:
            print(f"Name: {i['name']}, Branch: {i['branch']}")


school = School("Atatürk İlkokulu", 1984)
school.add_new_student("Kemal", "5B")
school.add_new_student("Ayşe", "6A")
school.add_new_teacher("Yunus", "OOP")
school.add_new_teacher("Yavuz", "Music")
school.view_student_list()
school.view_teacher_list()





