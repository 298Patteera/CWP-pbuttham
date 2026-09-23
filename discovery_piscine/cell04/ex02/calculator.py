def plus(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2 

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error"
    return num1 / num2

def main():
    num1 = int(input("Give me the first number: "))
    num2 = int(input("Give me the second number: "))

    print(f"Thank you!")
    print(f"{num1} + {num2} = {plus(num1, num2)}")
    print(f"{num1} - {num2} = {minus(num1, num2)}")    
    print(f"{num1} / {num2} = {int(divide(num1, num2))}")
    print(f"{num1} x {num2} = {multiply(num1, num2)}")

main()
