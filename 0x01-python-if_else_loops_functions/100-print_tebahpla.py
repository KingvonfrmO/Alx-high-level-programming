for i in range(122, 96, -1):
    if i % 2 == 0:
        output = "{}".format(chr(i))
    else:
        output = "{}".format(chr(i - 32))

    print(output, end="")