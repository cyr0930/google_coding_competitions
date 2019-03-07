def solution(p, picks, bans):
    n = len(picks)
    counts1 = [0] * p
    counts2 = [0] * p
    for pick in picks:
        for i in range(p):
            if int(pick[i]):
                counts1[i] += 1
            else:
                counts2[i] += 1

    while(True):
        for i in range(p):
            max1 = max(counts1)
            max2 = max(counts2)
            if max1 > max2:
                idx = counts1.index(max1)
            else:
                idx = counts1.index(max1)
    return 0


inputFile = open('B.in', 'r')
outputFile = open('B.out', 'w')

numOfTests = int(inputFile.readline())
for i in range(numOfTests):
    print(i)
    N, M, P = tuple(map(lambda x: int(x), inputFile.readline().split()))

    picks = []
    for j in range(N):
        picks.append(inputFile.readline())
    bans = []
    for j in range(M):
        bans.append(inputFile.readline())

    answer = solution(P, picks, bans)
    outputFile.write(f'Case #{i+1}: {answer}\n')

inputFile.close()
outputFile.close()
