def solution(N, O, D, X_1, X_2, A, B, C, M, L):
    if D < 0:
        return 'IMPOSSIBLE'
    S = [X_1, X_2]
    for i in range(2, N):
        S.append((A*S[len(S)-1] + B*S[len(S)-2] + C) % M)
    count = 0
    total = 0
    max_sweet = 0
    start = 0
    contains_zero = False
    for i in range(N):
        if S[i] == 0:
            contains_zero = True
        total += S[i]
        count += 0 if S[i] % 2 == 0 else 1
        while total > D or count > O:
            total -= S[start]
            count -= 0 if S[start] % 2 == 0 else 1
            start += 1
        if total > max_sweet:
            max_sweet = total
    return str(max_sweet) if max_sweet > 0 or contains_zero else 'IMPOSSIBLE'


inFile = open("A_s-small-practice.in", "r")
outFile = open("A_s.out", "w")
T = int(inFile.readline())
for i in range(T):
    print(i)
    N, O, D = map(lambda x: int(x), inFile.readline().split())
    X_1, X_2, A, B, C, M, L = map(lambda x: int(x), inFile.readline().split())
    outFile.write("Case #" + str(i+1) + ": " + str(solution(N, O, D, X_1, X_2, A, B, C, M, L)) + "\n")
inFile.close()
outFile.close()
