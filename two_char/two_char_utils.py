def get_char(Cin):
    Char = tuple(set(Cin))
    if len(Char) < 2:
        return 0
    length = []
    for i in range(len(Cin) - 1):
        for j in range(i + 1, len(Cin)):
            test = "".join([a for a in Cin if a in (Cin[i], Cin[j])])
            if any(test[k] == test[k+1] for k in range(len(test) - 1)):
                continue
            else:
                length.append(len(test))

    if length:
        return max(length)
    return 0

if __name__ == '__main__':
    Cin = input()
    print(get_char(Cin))