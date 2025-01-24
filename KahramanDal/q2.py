# ANSWER2:
class School:
    def __init__(self, name, foundation_year):
        self.name= name
        self.foundaion_year =foundation_year
        self.students=[]
        self.teachers={}

    def add_new_student(self, student_name, student_class):
        self.students.append({'name':student_name,'class':student_class})
        print(f'{student_name} has been added to the {student_class} class.')
    
    def add_new_teacher(self,teacher_name, major):
        self.teachers[teacher_name]=major
        print(f'{teacher_name} has been added to the {major} department.')

    def view_student_list(self):
        print("\nStudent List:")
        for student in self.students:
            print(f"Name: {student['name']}, Class: {student['class']}")

    def view_teacher_list(self):
        print("\nTeacher List:")
        for teacher_name,major in self.teachers.items():
            print(f"Name: {teacher_name}, Major: {major}")

school = School("Yavuz Selim College", 1991)

school.add_new_student("Ahmet", "10th Grade")
school.add_new_student("Ayşe", "11th Grade")
school.add_new_teacher("Ali", "Mathematics")
school.add_new_teacher("Veli", "Physics")  
school.view_student_list()
school.view_teacher_list()
