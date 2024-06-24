def create_pattern(line):
    for i in range(line):
        s = ""
        for j in range(i + 1):
            s += "*"
        print(s)


create_pattern(4)
