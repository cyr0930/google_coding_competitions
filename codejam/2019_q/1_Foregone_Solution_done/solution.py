def solution(N):
    A, B = 0, 0
    mult = 1
    while N > 0:
        q, r = divmod(N, 10)
        if r == 5:
            A, B = A + mult * 2, B + mult * 3
        elif r == 0:
            A, B = A + mult, B + mult * 9
            q -= 1
        else:
            A, B = A + mult, B + mult * (r - 1)
        mult *= 10
        N = q
    print(A+B)
    return str(A) + ' ' + str(B)


def main():
    T = int(input())
    for t in range(T):
        N = int(input())
        answer = solution(N)
        print('Case #' + str(t+1) + ': ' + answer)


if __name__ == '__main__':
    main()
