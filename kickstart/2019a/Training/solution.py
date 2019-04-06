def solution(N, P, S):
    S.sort()
    minVal = 0
    for i in range(P-1):
        minVal += S[P-1] - S[i]
    cur = minVal
    for i in range(P, N):
        cur -= S[i-1] - S[i-P]
        cur += (S[i] - S[i-1]) * (P-1)
        if cur < minVal:
            minVal = cur
    return minVal


def main():
    T = int(input())
    for t in range(T):
        N, P = input().split()
        N, P = int(N), int(P)
        S = [int(x) for x in input().split()]
        answer = solution(N, P, S)
        print('Case #' + str(t+1) + ': ' + str(answer))


if __name__ == '__main__':
    main()
