"""
Question2: Create a "School" class in Python. This class should have the following features and functionality:

Features:
"name"
"foundation_year"
"students"
"teachers"
Methods:
add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.
add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. It takes the teacher's name and major and adds it to the "teachers" dictionary.
view_student_list(self): A method used to display the list of students enrolled in the school. List student names and classes.
view_teacher_list(self): A method used to display the list of teachers working in the school. List teacher names and majors.
"""
class School:
    def __init__(self,school_name, foundation_year):
        self.school_name = school_name
        self.foundation_year = foundation_year
        self.students = []#ogrencileri tutacak bos liste
        self.teachers = {}#ogretmenlerin tutulacagi bos liste

    def add_new_student(self, student_name, student_class):
        self.students.append({"name": student_name, "class":student_class})

    def add_new_teacher(self,teacher_name, branch):
        self.teachers[teacher_name] = branch

    def view_student_list(self):
        for student in self.students:
            print(f"Name: {student['name']}, Class: {student['class']}")

    def view_teacher_list(self):
        for teacher, branch in self.teachers.items():
             print(f"Name: {teacher}, Branch: {branch}")

    # Okul nesnesi oluştur
school = School("Yıldız İlköğretim Okulu", 2000)

# Öğrenciler ekle
school.add_new_student("Ahmet", "5A")
school.add_new_student("Ayşe", "6B")
school.add_new_student("Mehmet", "4C")

# Öğretmenler ekle
school.add_new_teacher("Ali", "Matematik")
school.add_new_teacher("Ayşe", "Fen Bilgisi")
school.add_new_teacher("Fatma", "Türkçe")

# Öğrenci listesini görüntüle
print("Öğrenci Listesi:")
school.view_student_list()

# Öğretmen listesini görüntüle
print("\nÖğretmen Listesi:")
school.view_teacher_list()


