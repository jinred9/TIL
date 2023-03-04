# def subset_bit(idx, n):
#     global count
#     if idx == n:
#         print(visited)
#         count += 1
#     else:
#         visited[idx] = 1
#         subset_bit(idx+1, n)
#         visited[idx] = -1
#         subset_bit(idx+1, n)

# n = 4
# visited = [False for _ in range(n)]
# subset = []
# count = 0
# subset_bit(0, n)
# print(count)

a = []
for i in range(1, 101):
    a.append(i)
print(sum(a))
print(sum(a)/len(a))

