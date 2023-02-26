# 재귀함수로 부분집합 구하기======================================================================================
def subset_return(idx):
    global count
    # 현재 idx 가 집합(set_example)의 길이와 같다 => 부분 집합 완성
    if idx == len(set_example):
        count += 1
        print(subset)
        return
    subset.append(set_example[idx])
    subset_return(idx+1)

    subset.pop()
    subset_return(idx+1)

set_example = ['A', 'B', 'C', 'D', 'E']
subset = []
count = 0
subset_return(0)
print(count)

# DFS로 부분집합 구하기======================================================================================
def subset_dfs(idx):
    global count
    # 현재 idx 가 집합(set_example)의 길이와 같다 => 부분 집합 완성
    if idx == len(set_example):
        subset =[]
        for i in range(len(set_example)):
            if visited[i] == True:
                subset.append(set_example[i])
        count += 1
        print(subset)
        return
    # for i in range(len(set_example)):
    #     if not visited[i]:
    else:
        visited[idx] = True
        subset_dfs(idx+1)
        visited[idx] = False
        subset_dfs(idx+1)
    
set_example = ['A', 'B', 'C', 'D', 'E']
visited = [False for _ in range(len(set_example))]
subset = []
count = 0
subset_dfs(0)
print(count)

# DFS로 n까지의 부분집합 구하기======================================================================================
def DFS(v):
    if v==n+1:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
        print()
    else:
        ch[v]=1
        DFS(v+1)
        ch[v]=0
        DFS(v+1)

n=5
ch=[0]*(n+1)
DFS(1)

# 순열모듈로 부분집합 구하기======================================================================================
from itertools import permutations, combinations

def subset_per(idx):
    global count
    for i in range(len(set_example)):
        count += len(list(combinations(set_example, i)))
        print(list(combinations(set_example, i)))
    print(count)


set_example = ['A', 'B', 'C', 'D', 'E']
visited = [False for _ in range(len(set_example))]
subset = []
count = 1
subset_per(0)

# 2**n 부분집합 구하기======================================================================================
def subset_bit(idx, n):
    global count
    if idx == n:
        print(visited)
        count += 1
    else:
        visited[idx] = 1
        subset_bit(idx+1, n)
        visited[idx] = -1
        subset_bit(idx+1, n)

n = 4
visited = [False for _ in range(n)]
subset = []
count = 0
subset_bit(0, n)
print(count)

# m**n 부분집합 구하기======================================================================================
def subset_num(idx, n):
    global count
    if idx == n:
        print(visited)
        count += 1
    else:
        for i in set_example:
            visited[idx] = i
            subset_num(idx+1, n)

n = 4
set_example = ['A', 'B', 'C']
visited = [False for _ in range(n)]
count = 0
subset_num(0, n)
print(count)