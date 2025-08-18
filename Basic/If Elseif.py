input1 = int(input("Ente the marks: "))

def Grade(input1):
    if input1 >= 70:
        print("Grade A")
    elif input1 >= 60:
        print("Grade B")
    elif input1 >= 50:
        print("Grade C")
    elif input1 >= 40:
        print("Grade D")
    else: 
        print("Fail")
Grade(input1)
