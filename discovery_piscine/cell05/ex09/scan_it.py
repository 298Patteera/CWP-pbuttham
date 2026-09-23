import sys

if len(sys.argv) != 3:
    print("none")
else:
    kw = sys.argv[1]
    txt = sys.argv[2]

    if kw in txt:
        print(txt.count(kw))
    else:
        print("none")