mult_dict = {}
pow_dict = {}


def solution(n, m):
    mult_dict[(m, m)] = 1
    for i in range(1, m+1):
        mult_dict[(m, m-i)] = mult_dict[(m, m-i+1)] * (m-i+1) % 1000000007
    for i in range(m+1, 2*n-m+1):
        mult_dict[(i, m)] = mult_dict[(i-1, m)] * i % 1000000007
    mult_dict[(2*n-m, 2*n-m)] = 1
    for i in range(2*n-m+1, 2*n+1):
        mult_dict[(i, 2*n-m)] = mult_dict[(i-1, 2*n-m)] * i % 1000000007
    for i in range(m+1):
        buf = mult_dict[(2 * n - i, 2 * n - m)] * mult_dict[(2 * n - m, m)] % 1000000007
        mult_dict[(2 * n - i, m-i)] = buf * mult_dict[(m, m-i)] % 1000000007
    pow_dict[0] = 1
    for i in range(1, m+1):
        pow_dict[i] = pow_dict[i-1]*2 % 1000000007
    positive = True
    result = 0
    for i in range(m+1):
        buf = pow_dict[i] * mult_dict[(m, i)] % 1000000007
        buf = buf * mult_dict[(2*n-i, m-i)] % 1000000007
        result += (1 if positive else -1) * buf
        result %= 1000000007
        positive = not positive
    return result


inFile = open("C-large-practice.in", "r")
outFile = open("C.out", "w")
T = int(inFile.readline())
for i in range(T):
    print(i)
    N, M = map(lambda x: int(x), inFile.readline().split())
    outFile.write(f'Case #{i+1}: {solution(N, M)}\n')
inFile.close()
outFile.close()
