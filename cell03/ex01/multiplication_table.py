def multiplyLoop(num):
    for i in range(10):
        result = num * i
        print(f"{i} x {num} = {result}")

def main():
    num = int(input("Enter a number \n"))
    multiplyLoop(num)
main()
