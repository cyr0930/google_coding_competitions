def solution(N, L, ciphers):
    min_val = min(ciphers)
    min_idx = ciphers.index(min_val)
    ans = [None] * (L + 1)
    p, q = None, None
    for i in range(2, N+1):
        q, r = divmod(min_val, i)
        if r == 0:
            p = i
            break
    if min_idx == 0:
        if ciphers[1] % p == 0:
            p, q = q, p
    else:
        if ciphers[min_idx-1] % q == 0:
            p, q = q, p
    ans[min_idx], ans[min_idx+1] = p, q
    for i in range(min_idx-1, -1, -1):
        ans[i] = ciphers[i] // ans[i+1]
    for i in range(min_idx+2, len(ans)):
        ans[i] = ciphers[i-1] // ans[i-1]
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
