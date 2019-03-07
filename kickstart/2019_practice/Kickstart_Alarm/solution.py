def solution(N, K, x, y, C, D, E1, E2, F):
    A = [(x+y) % F]
    for i in range(2, N+1):
        x, y = (C * x + D * y + E1) % F, (D * x + C * y + E2) % F
        A.append((x+y) % F)
    ans = 0
    table = [0] * N
    f = 1000000007
    for i in range(N):
        cur = i+1
        for j in range(K):
            table[i] = (table[i] + ((cur**(j+1)) % f)) % f
    for i in range(N):
        cur_ans = 0
        for j in range(i+1):
            cur_ans = (cur_ans + table[j]) % f
        cur_ans = (cur_ans * (N - i)) % f
        cur_ans = (cur_ans * A[i]) % f
        ans = (ans + cur_ans) % f
    return ans


T = int(input())
for t in range(T):
    N, K, x1, y1, C, D, E1, E2, F = map(lambda x: int(x), input().split())
    answer = solution(N, K, x1, y1, C, D, E1, E2, F)
    print(f'Case #{t+1}: {answer}')
