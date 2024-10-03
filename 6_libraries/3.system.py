import sys


if len(sys.argv) < 2:
    sys.exit("Few Arguments")

for arg in sys.argv[1:]:
    print("my name is", arg)
