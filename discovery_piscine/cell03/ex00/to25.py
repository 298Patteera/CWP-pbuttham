def inputCheck(num):
    if num > 25:
        return print(f"Error")
    else :
        return num

def loopTil25(num):
    while num <= 25:
        print(f"Inside the loop, my variable is {num}")
        num += 1  

def main():
    num = int(input("Enter a number less than 25 \n"))
    inputCheck(num)
    loopTil25(num)
main()
