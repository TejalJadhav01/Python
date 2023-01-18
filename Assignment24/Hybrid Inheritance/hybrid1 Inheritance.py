class book():
    def __init__(self):
        self.b_name = "harry potter"
        self.author = "j.k.rowling"
        self.price = "2000"
        self.publisher = "bloomsbury"
        self.parts = "8"
    def B_details(self):
        print("Book Details : ","b_name :" ,self.b_name,"author :",self.author,"price :",self.price,"publisher : ",self.publisher,"parts :",self.parts)

class B_author(book):
    def __init__(self):
        self.name = "j.k.rowling"
        self.country = "UK"
        self.age = 53
        self.dob = "23/9/1969"
        book.__init__(self)
        
    def A_details(self):
        print("Author Details : ","name : ",self.name,"country : ",self.country,"age : ",self.age,"DOB : ",self.dob)

class B_publisher(B_author,book ):
    def __init__(self):
        self.name = "bloomsbury"
        self.country = "UK"
        self.age = 53
        B_author.__init__(self)
        book.__init__(self)

    def p_details(self):
        print("Publisher Details : ","name : ",self.name,"country : ",self.country,"age : ",self.age)

b = B_publisher()
b.B_details()
b.A_details()
 
