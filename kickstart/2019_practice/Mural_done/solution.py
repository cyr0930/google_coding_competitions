def solution(n, line):
    k = int(len(line)/2) if len(line) % 2 == 0 else int(len(line)/2+1)
    cur = 0
    for i in range(k):
        cur += int(line[i])
    maxVal = cur
    for i in range(1, int(len(line)/2+1)):
        cur -= int(line[i-1])
        cur += int(line[i+k-1])
        if maxVal < cur:
            maxVal = cur
    return maxVal


T = int(input())
for t in range(T):
    N = int(input())
    line = input().rstrip()
    answer = solution(N, line)
    print(f'Case #{t+1}: {answer}')
