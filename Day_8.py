# LEET_CODE
#  26. Remove Duplicates from Sorted Array

def dup(arr):
    s = 0
    for f in range(1,len(arr)):
        if arr[f] != arr[s]:
            s += 1
            arr[s] = arr[f]
    return s + 1

# 125. Valid Palindrome
def palindrome(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

# 167. Two Sum II - Input Array Is Sorted
def TwoSum(arr, tar):
    left = 0
    right = len(arr) - 1

    while left < right:
        s = arr[left] + arr[right]
        if s == tar:
            return True
        elif s < tar:
            left += 1
        else:
            right -= 1

    return False

# 283. Move Zeroes
def moveZero(a):
    x = 0
    for y in range(1,len(a)):
        if a[x] != 0:
            x+=1
        elif a[x]==0 and a[y]!=0:
            a[x],a[y] = a[y],a[x]
            x+=1
    return a

# 344. Reverse String
def stringRev(sr):
    s,r = 0,len(sr)-1
    while s < r:
        sr[s],sr[r] = sr[r],sr[s]
        s += 1
        r -= 1
    return sr



