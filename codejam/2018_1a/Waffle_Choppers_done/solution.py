def solution(R, C, H, V, pancake):
    colCount = [0] * C
    for row in pancake:
        for i in range(C):
            if row[i] == '@':
                colCount[i] += 1
    count = sum(colCount)
    q1, r1 = divmod(count, H+1)
    if r1 != 0:
        return False
    q2, r2 = divmod(count, V+1)
    if r2 != 0:
        return False
    q3, r3 = divmod(q1, V+1)
    if r3 != 0:
        return False
    compressedCount = 0
    for c in colCount:
        if c != 0:
            compressedCount += 1
    cur = 0
    idx = 0
    compressed = []
    for i in range(H + 1):
        compressed.append([0] * compressedCount)
    for row in pancake:
        ci = 0
        for i in range(C):
            if colCount[i] == 0:
                continue
            if row[i] == '@':
                cur += 1
                compressed[idx][ci] += 1
            ci += 1
        if cur > q1:
            return False
        elif cur == q1:
            cur = 0
            idx += 1
    idx = 0
    while idx < compressedCount:
        cand = set(range(compressedCount))
        for row in compressed:
            curCand = set()
            cur = 0
            for i in range(idx, compressedCount):
                cur += row[i]
                if cur == q3:
                    curCand.add(i)
                    if i == compressedCount-1 or row[i+1] != 0:
                        break
            cand &= curCand
            if not cand:
                return False
        idx = next(iter(cand)) + 1
    return True


T = int(input())
for it in range(T):
    R, C, H, V = map(lambda x: int(x), tuple(input().split()))
    pancake = []
    for i in range(R):
        pancake.append(input())
    answer = 'POSSIBLE' if solution(R, C, H, V, pancake) else 'IMPOSSIBLE'
    print(f'Case #{it+1}: {answer}\n')
