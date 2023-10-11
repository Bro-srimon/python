print("Enter a number ot ascending order, descending order")
def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    return a / b

def pow(a,b):
    return a ** b

def per(a,b):
    return a % b


while True :

    print("Please select operation - \n" \
        "1. Calculator \n" \
        "2. Power and Exponents \n" \
        "3. Ascending and Descending order \n")

    Choice = int(input("Enter Choice (1/2/3): "))

    if Choice == 1 :
        
        print(".")
        print("Calculator :- \n" \
        "1. Add \n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n" \
        "5. Percentage\n")

        Choice1 = int(input("Enter Choice (1/2/3/4): "))
        
        print(".")
        
        a = float(input("Enter 1st number: "))
        b = float(input("Enter 2nd number: "))
        
        print(".")
        
        if Choice1 == 1:

            print(a,"+",b,"=",add(a,b))
            print(".")

        if Choice1 == 2:

            print(a,"-",b,"=",sub(a,b))
            print(".")

        if Choice1 == 3:

            print(a,"x",b,"=",mul(a,b))
            print(".")

        if Choice1 == 4:

            print(a,"÷",b,"=",div(a,b))
            print(".")

        if Choice1 == 5:

            print(a,"%",b,"=",per(a,b))
            print(".")

    if Choice == 2:

        print("Power and Exponents :- \n")

        a = float(input("Enter a number : "))
        b = float(input("Enter a power : "))

        print(a,"is power by",b,"is",pow(a,b))
    
    if Choice == 3:

        print("Ascending and Descending order :- \n")

        b = int(input("Enter how many numbers you have : "))
        c = []
        for i in range(b):
            a = int(input("Enter a number: "))
            c.append(a)
        A = input("Enter A for ascending order or enter D for descending order: ")
        d = []
        if A=="A":
            for i in range(b):
                d.append(min(c))
                c.remove(min(c))
            print("The ascending order is: ",*d)
        elif A=="D":
            for i in range(b):
                d.append(max(c))
                c.remove(max(c))
            print("The descending order is: ",*d)