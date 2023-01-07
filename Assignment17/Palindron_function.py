def palindron(string):
    rev = string[: : -1]
    if(string == rev):
        print("string is palindron")
    else:
        print("string is  not palindron")
    return string

x = input("Enter string : ")

palindron(x)