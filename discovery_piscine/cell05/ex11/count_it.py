import sys

if len(sys.argv) == 1:
    print("none")
else:
    print(f"parameters: {len(sys.argv) - 1}")

    #sys.argv[1:] cuz sys.argv[0] is program name, so don't count
    for para in sys.argv[1:]:
        print(f"{para}: {len(para)}")