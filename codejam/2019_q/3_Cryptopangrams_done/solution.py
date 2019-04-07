def gcd(m, n):
    while n != 0:
        m, n = n, m % n
    return m


def solution(L, ciphers):
    idx = None
    for i in range(1, L):
        if ciphers[i-1] != ciphers[i]:
            idx = i
            break
    b = gcd(ciphers[idx-1], ciphers[idx])
    a = ciphers[idx-1] // b
    return de_cipher(L, idx, a, b, ciphers)


def de_cipher(L, idx, a, b, ciphers):
    ans = [None] * (L + 1)
    ans[idx-1] = a
    ans[idx] = b
    for i in range(idx-2, -1, -1):
        ans[i] = ciphers[i] // ans[i+1]
    for i in range(idx+1, L+1):
        ans[i] = ciphers[i-1] // ans[i-1]
    s = list(set(ans))
    s.sort()
    A = ord('A')
    d = {prime: chr(A + i) for i, prime in enumerate(s)}
    return ''.join([d[prime] for prime in ans])


def main():
    T = int(input())
    for t in range(T):
        N, L = input().split()
        ciphers = [int(x) for x in input().split()]
        answer = solution(int(L), ciphers)
        print('Case #' + str(t+1) + ': ' + answer)


if __name__ == '__main__':
    main()
