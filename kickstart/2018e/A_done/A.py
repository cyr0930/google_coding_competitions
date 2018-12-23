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


inputFile = open('A-large-practice.in', 'r')
outputFile = open('A.out', 'w')

numOfTests = int(inputFile.readline())
for i in range(numOfTests):
    N, K = tuple(map(lambda x: int(x), inputFile.readline().split()))
    data = map(lambda x: int(x), inputFile.readline().split())
    answer = solution(N, K, data)
    outputFile.write('Case #' + str(i+1) + ': ' + str(answer) + '\n')

inputFile.close()
outputFile.close()
