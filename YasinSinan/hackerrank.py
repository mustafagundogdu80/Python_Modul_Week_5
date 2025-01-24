"""
Inheritance: https://www.hackerrank.com/challenges/inheritance/problem
"""
class person:
    def __init__(self, first_name, last_name, id):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
    def info(self):
        print (f"first name:",self.first_name, "last_name: ", self.last_name, "id:" ,self.id)
class student(person):
    def __init__(self, first_name, last_name, id, scores):
        super().__init__(self, first_name, last_name, id)
        self.scores=scores
    def info(self):
        print (f"first name:",self.first_name, "last_name: ", self.last_name, "id:" ,self.id,"scores",self.scores )
    def calculate(self):
        average=sum(self.scores)/len(self.scores)
        if average >=90 and average <=100:
            return "O"
        elif average >=80 and average <90:
            return "E"
        elif average >=70 and average <80:
            return "A"
        elif average >=55 and average <70:
            return "P"
        elif average >=40 and average <55:
            return "D"
        elif average >=0 and average <40:
            return "T"
        else :
            return "score is invalid"
student = student("Yasin", "Sinan", 12345, [95, 85, 80, 70])
print (student)
print (f"self.first_name :{first_name}, self.last_name: {last_name},  self.id: {id}\n ,self.scores:{scores}\n, self.scores sep=")
"""--------------------------------------------------------------------"""

"""
Classes: Dealing with Complex Numbers: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem
"""
