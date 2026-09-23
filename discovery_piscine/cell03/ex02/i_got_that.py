def main():
    user_say = input("What you gotta say? : ")

    if user_say != "STOP":
        while True:
            user_say_else = input("I got that! Anything else? : ")
            if user_say_else == "STOP":
                return False

main()