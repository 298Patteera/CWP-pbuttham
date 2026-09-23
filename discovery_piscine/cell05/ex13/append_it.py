import sys

if len(sys.argv) == 1:
    print("none")
else:
    for para in sys.argv[1:]:
        if not para.endswith("ism"):
            print(para + "ism")