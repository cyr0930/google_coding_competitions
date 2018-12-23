def non_zero_solution(A, counter):
    count = 0
    while len(A) > 2:
        start = 0
        end = len(A) - 2
        target = A[len(A) - 1]
        while start < end:
            mult = A[start] * A[end]
            if mult < target:
                start += 1
            elif mult > target:
                end -= 1
            else:
                count += counter[A[start]] * counter[A[end]] * counter[target]
                start += 1
        if counter[A[start]] > 1 and A[start] * A [start] == target:
            count += counter[A[start]]*(counter[A[start]]-1)/2*counter[target]
        A.pop()
    return count


def solution(n, l):
    counter = {}
    singleA = []
    for i in l:
        if i in counter:
            counter[i] += 1
        else:
            counter[i] = 1
            if i > 1:
                singleA.append(i)
    sorted(singleA)
    numOfZeroSet = 0 if 0 not in counter or counter[0] < 2\
        else counter[0]*(counter[0]-1)/2*(n-counter[0])\
             + (0 if counter[0] < 3 else counter[0]*(counter[0]-1)*(counter[0]-2)/6)
    numOfOneSet = 0 if 1 not in counter or counter[1] < 3\
        else counter[1]*(counter[1]-1)*(counter[1]-2)/6
    if 1 in counter:
        for i in singleA:
            if counter[i]> 1:
                numOfOneSet += counter[i]*(counter[i]-1)/2 * counter[1]*(counter[1]-1)/2
    return int(numOfZeroSet + numOfOneSet + non_zero_solution(singleA, counter))


inputFile = open('A-large-practice.in', 'r')
outputFile = open('A.out', 'w')

numOfTests = int(inputFile.readline())
for it in range(numOfTests):
    N = int(inputFile.readline())
    data = map(lambda x: int(x), inputFile.readline().split())
    answer = solution(N, sorted(data))
    outputFile.write('Case #' + str(it+1) + ': ' + str(answer) + '\n')
    outputFile.flush()

inputFile.close()
outputFile.close()
