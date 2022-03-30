# 1
# import itertools
# arr = [1, 2, 3]
# new_arr = itertools.permutations(arr)
# counter_of_be_groups = 0
# for group in new_arr:
#     sum = 0
#     i = 1
#     for el in group:
#         sum += el * i
#         i += 1
#     if sum % 2 == 0:
#         counter_of_be_groups += 1
# print(counter_of_be_groups)

n = int(input())
m = [[None]*n for i in range(n)]
p = ord('z')-ord('a')
border = n//2+n % 2

for i in range(border):
    for j in range(border):
        m[i][j] = chr(ord('a')+abs(i-j) % p)
    for j in range(border, n):
        m[i][j] = m[i][n-j-1]
for i in range(border, n):
    m[i] = m[n-i-1]
for j in range(n):
    print(m[j])

