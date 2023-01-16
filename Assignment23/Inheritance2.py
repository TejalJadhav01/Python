class book():
    def __init__(self):
        self.b_name = "harry potter"
        self.author = "j.k.rowling"
        self.price = "2000"
        self.publisher = "bloomsbury"
        self.parts = "8"
    def B_details(self):
        print("b_name :" ,self.b_name,"author :",self.author,"price :",self.price,"publisher : ",self.publisher,"parts :",self.parts)

class B_author(book):
    def __init__(self):
        self.name = "j.k.rowling"
        self.country = "UK"
        self.age = 53
        self.dob = "23/9/1969"
        book.__init__(self)
    def A_details(self):
        print("name : ",self.name,"country : ",self.country,"age : ",self.age,"DOB : ",self.dob)

b = B_author()
b.B_details()
b.A_details()
