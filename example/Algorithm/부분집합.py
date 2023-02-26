# 재귀함수로 부분집합 구하기
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
visited = [False for _ in range(len(set_example)+1)]
subset = []
count = 0
print(count)