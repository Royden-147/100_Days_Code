# 3. Longest Substring Without Repeating Characters
def lenSubString(s):
    a = b = 0
    max_len = 0
    c = set()
    while b < len(s):
        if s[b] not in c:
            c.add(s[b])
            max_len = max(max_len,b-a+1)
            b += 1
        else:
            c.remove(s[a])
            a+=1
    return max_len
x = 'aba'
print(lenSubString(x))

# 11. Container With Most Water
def maxWCap(w):
    f,r = 0,len(w)-1
    cap = 0
    while f < r:
        a = ((min(w[f],w[r]))*(r-f))
        cap = max(cap,a)
        if w[f] <= w[r]:
            f += 1
        else:
            r -= 1
    return cap

wat = [1,8,6,2,5,4,8,3,7]
print(maxWCap(wat))

# 121. Best Time to Buy and Sell Stock
def stock1(prices):
    l, r = 0, 1
    max_profit = 0

    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
        else:
            l = r
        r += 1
    return max_profit
v = [2, 1, 4]
print(stock1(v))
