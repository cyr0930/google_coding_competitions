def solution(n, k, l):
    l = sorted(l)
    day = 0
    capacity = 0
    consume = 0
    for a in l:
        if a > day:
            consume += 1
            capacity += 1
            if capacity >= k:
                capacity = 0
                day += 1
    return consume


numOfTests = int(input())
for i in range(numOfTests):
    N, K = tuple(map(lambda x: int(x), input().split()))
    data = map(lambda x: int(x), input().split())
    answer = solution(N, K, data)
    print('Case #' + str(i+1) + ': ' + str(answer) + '\n')
