def remDup(s):
    ch = list(s)
    a = set()
    i = 0
    for j in range(len(ch)):
        if ch[j] not in a:
            a.add(ch[j])
            ch[i]=ch[j]
            i += 1
    return ch[:i]
s = 'programming'
print(remDup(s))