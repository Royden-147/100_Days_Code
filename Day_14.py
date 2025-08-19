def validPara(ar):
    f = []
    d = {
        ')':'(',
        '}':'{',
        ']':'['
    }
    for i in ar:
        if i in d:
            if f and f[-1] == d[i]:
                f.pop()
            else:
                return False
        else:
            f.append(i)
    return not f
s = "]"
print(validPara(s))
