import sys

def downcase_it(txt):
    return txt.lower()

def main():
    if len(sys.argv) == 1:
        print("none")
    else:
        for txt in sys.argv[1:]:
            print(f"{downcase_it(txt)}")

main()
