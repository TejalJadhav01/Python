
class Laptop():
    def __init__(self):
        self.name = "Dell"
        self.processor = "intel core i3"
        self.RAM = " 4 GB "
        self.OS = " 32 bit "

    def configuration(self):
        print("Name is : " , self.name)
        print("processor is : " , self.processor)
        print("RAM is : " , self.RAM)
        print("OS is : " , self.OS)

        
L1 = Laptop()
L2 = Laptop()

L1.configuration()

L2.name = L2.name + " Laptop"
L2.OS = "64 bit"
print(" New name is" , L2.name)
print(" New OS is" , L2.name)


