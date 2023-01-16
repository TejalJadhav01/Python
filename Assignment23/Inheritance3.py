class Google:
    def __init__ (self):
        self.name = " Google "
        self.country = " US"
        self.NO_of_Employee = 139,995
        self.founders = "Sergry Brin"
        self.CEO = " Sundar Pichai"

    def c_details(self):
        print("name :" , self.name , "Country :" , self.country,"NO. of Employee : ", self.NO_of_Employee , "founders : " , self.founders , " CEO : " ,self.CEO )

class CEO1(Google):
    def __init__(self):
        self.google_CEO = " Sundar Pichai "
        self.city = "Indian"
        self.age = "50"
        self.state = "Tamil Nadu"
        self.qualification = "BTech , MS , MBA "
        Google.__init__(self)
    def CEO1_details(self):
        print("google_CEO name : ", self.google_CEO , " city : " ,self.city , "age : ",self.age , "state : " , self.state , "qualification : " , self.qualification )
            
c = CEO1()
c.c_details()
c.CEO1_details()
