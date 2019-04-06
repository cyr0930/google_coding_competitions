def solution(N, L, ciphers):
    ans = []
    p, q = None, None
    for i in range(2, N+1):
        q, r = divmod(ciphers[0], i)
        if r == 0:
            p = i
            break
    if ciphers[1] % p == 0:
        p, q = q, p
    ans.append(p)
    ans.append(q)
    for i in range(2, L+1):
        ans[i] = ciphers[i-1] // ans[-1]
    s = list(set(ans))
    s.sort()
    A = ord('A')
    d = {prime: chr(A+i) for i, prime in enumerate(s)}
    return ''.join([d[prime] for prime in ans])


def main():
    T = int(input())
    for t in range(T):
        N, L = input().split()
        N, L = int(N), int(L)
        ciphers = [int(x) for x in input().split()]
        answer = solution(N, L, ciphers)
        print('Case #' + str(t+1) + ': ' + answer)


if __name__ == '__main__':
    main()
