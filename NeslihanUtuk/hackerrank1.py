#https://www.hackerrank.com/challenges/inheritance/problem


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    # Class Constructor
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores

    # Function Name: calculate
    # Return: A character denoting the grade.
    def calculate(self):
        average = sum(self.scores) / len(self.scores)
        if 90 <= average <= 100:
            return 'O'  # Outstanding
        elif 80 <= average < 90:
            return 'E'  # Exceeds Expectations
        elif 70 <= average < 80:
            return 'A'  # Acceptable
        elif 55 <= average < 70:
            return 'P'  # Passing
        elif 40 <= average < 55:
            return 'D'  # Poor
        else:
            return 'T'  # Troll


# Input Handling
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())  # Number of scores (not used in Python)
scores = list(map(int, input().split()))

# Create a Student object
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
