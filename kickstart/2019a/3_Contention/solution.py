def solution(N, Q, l):
    l.sort(key=lambda x: x[1] - x[0])
    s = N
    ans = []
    for i in range(len(l)):
        t = l[i]
        if not ans:
            ans.append(t)
        else:
            buf = []
            diff = 0
            for idx in ans:
                if idx[1] < t[0]-1:
                    buf.append(idx)
                else:
                    if idx[1] >= t[1]:
                        return 0
                    t[0] = idx[0]
        s = min(s, count)
    return s


def main():
    T = int(input())
    for t in range(T):
        N, Q = input().split()
        N, Q = int(N), int(Q)
        l = []
        for i in range(Q):
            L, R = input().split()
            l.append((int(L), int(R)))
        answer = solution(N, Q, l)
        print('Case #' + str(t+1) + ': ' + str(answer))


if __name__ == '__main__':
    main()
