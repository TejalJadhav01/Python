class calculator():
    def __init__(self):
        self.a = 2
        self.b = 1
    def add(self):
        c=self.a + self.b
        print("Add is : ", c)
        
    def sub(self):
        c=self.a - self.b
        print("sub is : ", c)
        
    def mul(self):
        c=self.a * self.b
        print("mul is : ", c)

    def div(self):
        c=self.a / self.b
        print("div is : ", c)

a = calculator()
a.add()
a.sub()
a.mul()
a.div()
