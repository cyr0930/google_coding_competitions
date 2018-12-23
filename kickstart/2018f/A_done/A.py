def solution(L, A, B):
    subSet = set()
    for i in range(L):
        for j in range(0, L-i):
            subString = []
            for k in range(j, j+i+1):
                subString.append(B[k])
            subString.sort()
            subSet.add(''.join(subString))
    count = 0
    for i in range(L):
        for j in range(0, L-i):
            subString = []
            for k in range(j, j+i+1):
                subString.append(A[k])
                subString.sort()
            count += 1 if ''.join(subString) in subSet else 0
    return count


inFile = open("A-large-practice.in", "r")
outFile = open("A.out", "w")
T = int(inFile.readline())
for i in range(T):
    L = int(inFile.readline())
    A = inFile.readline()
    B = inFile.readline()
    outFile.write("Case #" + str(i+1) + ": " + str(solution(L, A, B)) + "\n")
inFile.close()
outFile.close()
