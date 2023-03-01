def solution(command):
    answer = [0, 0]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    idx = 0

    for char in command:
        if char == 'R':
            idx = (idx + 1) % 4
        elif char == 'L':
            idx = (idx - 1) % 4
        elif char == 'G':
            answer[0] += dx[idx]
            answer[1] += dy[idx]
        elif char == 'B':
            answer[0] -= dx[idx]
            answer[1] -= dy[idx]

    return answer

# [2, 2]
print(solution('GRGLGRG'))

# [2, 0]
print(solution('GRGRGRB'))
