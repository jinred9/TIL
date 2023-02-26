
n = 10
# 방법 1. 일반 함수 사용 방식 (Function)
def fib1(n):
    a,b = 0,1
    if n == 0:
        return 0
    elif n <= 2:
        return 1
        
    for i in range(0, n):
        a, b = b, a + b
    return a
print("일반 함수 사용 방식 : ", [fib1(x) for x in range(0, n+1)])
# [0, 1, 1, 2, 3, 5]


# 방법2. 재귀함수 사용 방식 (Recursive Function)
def fib2(n):
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)
print("재귀함수 사용 방식 : ", [fib2(x) for x in range(0, n+1)])
# [0, 1, 1, 2, 3, 5]


# 방법 3. 제네레이터 구현 방식 (Generator method)
def fib3(n):
    a, b = 0, 1
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    for i in range(0, n+1):
        yield a
        a,b = b, a+b
arr =[]
for i in fib3(n):
    arr.append(i)
print("제네레이터 구현 방식 : ", arr)
# [0, 1, 1, 2, 3, 5]


# 방법 4. 메모이제이션 구현 방법 (Memoization Method)
def fib4(n):
    if 'fibdic' not in globals():
        global fibdic
        fibdic = {0:0, 1:1}
        return n
    elif n in fibdic:
        return fibdic[n]
    else:
        fibdic[n] = fib4(n-1) + fib4(n-2)
        return fibdic[n]
print("메모이제이션 구현 방법 : ")
for i in range(0, n+1):
    print(fib4(i), end=' ')
print('\n')
# [0, 1, 1, 2, 3, 5]


# 방법 5. 파이썬 람다를 사용한 한줄 코딩 1 (Single Line Code with lambda)
fib5 = lambda n: 0 if n == 0 else( 1 if n<=2 else fib5(n-1) + fib5(n-2))
print("람다를 사용한 한줄 코딩 1 : ", [fib5(x) for x in range(0, n+1)])
# [0, 1, 1, 2, 3, 5]


# 방법 6. 파이썬 람다를 사용한 한줄 코딩 2 (Single Line Code with lambda)
fib6 = lambda n, a=0, b=1 : a if n<=0 else fib6(n-1, b, a+b)
print("람다를 사용한 한줄 코딩 2 : ", [fib6(x) for x in range(0, n+1)])
# [0, 1, 1, 2, 3, 5]


# 방법 7. 행렬 연산 (Matrix Operational method) 구현 방식
import numpy as np
matrix_op = np.matrix( [ [1,1], [1,0] ] )
print("행렬 연산 : ", [(matrix_op**x)[0,1] for x in range(0, n+1)])
# [0, 1, 1, 2, 3, 5]

