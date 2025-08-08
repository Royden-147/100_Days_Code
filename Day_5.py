# Changing list element
def changeEle(ac, val, pos):
    if pos > len(ac):
        print("Invalid Index")
    ac[pos] = val
    print(f"{val} is updated at pos {pos}")
    return ac
ax = list(map(int,input().split()))
print(changeEle(ax,12,6))

# delete element in a list
d = [2,4,5,7,8,4]
i,b = 2,[]
for a in range(len(d)):
    if a != i:
        b.append(d[a])
print(b)

# right rotation of elements
def rightRot(a, q):
    if q == 0:
        return a
    a = [a[-1]] + a[:-1]
    return rightRot(a,q-1)

arr = list(map(int,input().split()))
i = int(input())
print(rightRot(arr,i))


# Left Rotation of List elements
def leftRot(b,r):
    if r == 0:
        return b
    b = b[1:] + [b[0]]
    return leftRot(b,r-1)

re = list(map(int,input().split()))
f = int(input())
print(leftRot(re,f))