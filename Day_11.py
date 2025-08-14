def mergeList(l1,l2,m,n):
    l = r = 0
    h = []
    while l<n and r<m:
        if l1[l] <= l2[r]:
            h.append(l1[l])
            l += 1
        else:
            h.append(l2[r])
            r += 1
    while l < m:
        h.append(l1[l])
        l += 1
    while r < n:
        h.append(l2[r])
        r += 1
    return h

a = [1,2,3,0,0,0]
b = [2,5,6]
print(mergeList(a,b,3,3))