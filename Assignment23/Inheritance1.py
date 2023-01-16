class college():
    def __init__(self):
        self.name = "AITRC"
        self.branch = "CSE,ETC,MECH"
    def C_details(self):
        print("College Details : ")
        print("name:", self.name , "branch:",self.branch)
class student(college):
    def __init__(self):
        self.Sname = "abcd"
        self.Sid = "02"
        college.__init__(self)
    def S_details(self):
        print(" \nStudent Details : ")
        print("Sname:",self.Sname,"Sid:",self.Sid)

s = student()
s.C_details()
s.S_details()
