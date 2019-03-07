def solution(A, B):
    return (A+B+1) // 2


T = int(input())
for t in range(T):
    A, B = input().split()
    A, B = int(A), int(B)
    N = int(input())
    words = []
    for i in range(N):
        guess = solution(A, B)
        print(guess, flush=True)
        response = input()
        if response == 'TOO_SMALL':
            A = guess
        elif response == 'TOO_BIG':
            B = guess-1
        else:
            break
