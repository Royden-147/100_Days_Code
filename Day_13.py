# 643. Maximum Average Subarray I
# def maxAvgSubA(f,x):
#     sw = sum(f[:x])
#     max_sum = sw
#
#     for j in range(x,len(f)):
#         sw += f[j] - f[j-x]
#         max_sum = max(sw,max_sum)
#
#     return max_sum / x
#
# s = list(map(int,input().split()))
# print(maxAvgSubA(s,4))

# 485. Max Consecutive Ones
# def maxOnes(zeo):
#     count = 0
#     max_count = 0
#
#     for num in zeo:
#         if num == 1:
#             count += 1
#             max_count = max(max_count, count)
#         else:
#             count = 0
#
#     return max_count
# z = [1,1,0,1,1,1]
# print(maxOnes(z))

#