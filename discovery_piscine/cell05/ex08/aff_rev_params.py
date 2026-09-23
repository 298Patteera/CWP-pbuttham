import sys

#sys.argv count program name as 1st parameter
#then if add only 1 parameter -> 1 parameter can't be reverse, so it's "none" 
if len(sys.argv) < 3:
    print("none")
else:
    for para in sys.argv[1:][::-1]:
        print(para)