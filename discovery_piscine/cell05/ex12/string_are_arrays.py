import sys

if len(sys.argv) != 2:
    print("none")
else:
    txt = sys.argv[1]

    if "z" not in txt:
        print("none")
    else:
        print("z" * txt.count("z"))