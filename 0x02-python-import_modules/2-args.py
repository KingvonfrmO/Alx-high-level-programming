import sys

count = len(sys.argv) - 1
if count == 0:
    print("{} arguments.".format(count))
elif count == 1:
    print("{} argument:".format(count))
else:
    print("{} argumets:".format(count))
    

for i in range(1, len(sys.argv)):
    print("{}: {}".format(i, sys.argv[i]))