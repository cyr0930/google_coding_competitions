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


inputFile = open('B-small-attempt1.in', 'r')
outputFile = open('B.out', 'w')
T = int(inputFile.readline())
for test in range(T):
    N = int(inputFile.readline())
    line = inputFile.readline().rstrip()
    answer = solution(N, line)
    outputFile.write('Case #' + str(test+1) + ': ' + str(answer) + '\n')
inputFile.close()
outputFile.close()
