import collections


def bfs(office, R, C):
    dq = collections.deque(list(office))
    seen = office.copy()
    depth = 0
    count = len(dq)
    while dq:
        if count == 0:
            depth += 1
            count = len(dq)
        cur = dq.popleft()
        count -= 1
        candidates = [(cur[0]-1, cur[1]), (cur[0], cur[1]-1), (cur[0], cur[1]+1), (cur[0]+1, cur[1])]
        for t in candidates:
            if t in seen or t[0] < 0 or t[1] < 0 or t[0] >= R or t[1] >= C:
                continue
            dq.append(t)
            seen.add(t)
    return depth


def solution(R, C, mat):
    office = set()
    for i in range(R):
        for j in range(C):
            if mat[i][j] == '1':
                office.add((i, j))
    prev = None
    mdt = None
    for i in range(R):
        for j in range(C):
            idx = (i, j)
            if idx in office:
                continue
            if prev is not None:
                office.remove(prev)
            office.add(idx)
            val = bfs(office, R, C)
            prev = idx
            if mdt is None or val < mdt:
                mdt = val
    return 0 if mdt is None else mdt


def main():
    T = int(input())
    for t in range(T):
        R, C = input().split()
        R, C = int(R), int(C)
        mat = []
        for i in range(R):
            mat.append(list(input()))
        answer = solution(R, C, mat)
        print('Case #' + str(t+1) + ': ' + str(answer))


if __name__ == '__main__':
    main()
