import sys

if len(sys.argv) != 2:
    print("none")
else:
    kw = sys.argv[1]
    txt = input("What was the parameter? ")

    if kw == txt:
        print("Good job!")
    else:
        print("Nope, sorry...")