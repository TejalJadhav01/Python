class computer_science():
    def Result(self):
        print("1st year marks of student is 60%")
        print("2nd year marks of student is 70%")
        print("3rd year marks of student is 75%")
        print("B-tech of the marks is 80%")

class Electronics():
    def Result(self):
        print("1st year marks of student is 75%")
        print("2nd year marks of student is 80%")
        print("3rd year marks of student is 85%")
        print("B-tech of the marks is 90%")

class Department():
    def percentage(self,p):
        p.Result()

d = Department()
E = Electronics()
d.percentage(E)
C = computer_science()
d.percentage(C)
