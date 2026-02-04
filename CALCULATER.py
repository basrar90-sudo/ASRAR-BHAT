#calculater code

def calculater():
    while True:
        print("\n===calculater===")
        num1 = int(input("ENTER THE FIRST NUMBER "))
        operator = input("ENTER THE OPERATOR(+,-,*,/):")
        num2 = int(input("ENTER THE 2ND NUMBER"))

        if (operator == "+"):
            print("sum = ",num1+num2)
        elif(operator == "-"):
            print("subtraction = ",num1-num2)
        elif(operator == "*"):
            print("multiplication =",num1*num2) 

        elif(operator == "/"):
            if num2 == 0:
             print("CAN'T BE DEVIDED BY ZERO")
            else:
             print("division",num1/num2)

        again = input("DO YOU WANT TO USE CALCULATER AGAIN? (YES/NO):")
        if (again.lower() != "yes"):
            break

calculater()