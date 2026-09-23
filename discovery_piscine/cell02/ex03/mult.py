def multiply(num1, num2):
    return num1 * num2

def isNeg(num):
    if num == 0:
        return ("The result is positive and negative.")
    elif num < 0:
        return ("The result is negative.")
    else:
        return ("The result is positive.")

def main():
    num1 = int(input("Enter the first number: "))
    print(f"{num1}")
    num2 = int(input("Enter the second number: "))
    print(f"{num2}")
    result = multiply(num1, num2)
    print(f"{num1} x {num2} = {result}")
    print(isNeg(result))
main()