def solution(n, p, forbidden):
    forbidden.sort()
    forbiddenSet = set(forbidden)
    i = 0
    j = 1
    while len(forbidden) > j:
        if forbidden[j].startswith(forbidden[i]):
            forbiddenSet.remove(forbidden[j])
        else:
            i = j
        j += 1
    result = 2 ** n
    for f in forbiddenSet:
        result -= 2 ** (n - len(f))
    return result


inputFile = open('A-large.in', 'r')
outputFile = open('A.out', 'w')
T = int(inputFile.readline())
for it in range(T):
    N, P = map(lambda x: int(x), tuple(inputFile.readline().split()))
    forbidden = []
    for i in range(P):
        forbidden.append(inputFile.readline()[:-1])
    answer = solution(N, P, forbidden)
    outputFile.write('Case #' + str(it+1) + ': ' + str(answer) + '\n')
    outputFile.flush()
inputFile.close()
outputFile.close()
