def solution(N, P):
    ans = []
    for c in P:
        ans.append('S' if c == 'E' else 'E')
    return ''.join(ans)


def main():
    T = int(input())
    for t in range(T):
        N, P = int(input()), input()
        answer = solution(N, P)
        print('Case #' + str(t+1) + ': ' + answer)


if __name__ == '__main__':
    main()
