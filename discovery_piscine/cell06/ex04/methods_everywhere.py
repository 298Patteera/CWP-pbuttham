import sys

def shrink(txt):
    return txt[:8]

def enlarge(txt):
    txt = txt + ("Z" * (8-len(txt)))
    return txt

def main():
    if len(sys.argv) == 1:
        print("none")
    else:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                print(f"{shrink(arg)}")
            elif len(arg) < 8:
                print(f"{enlarge(arg)}")
            else:
                print(f"{arg}")
main()
