def solution(N, L, words):
    l = [{} for i in range(L)]
    for word in words:
        for i in range(L):
            l[i].setdefault(word[i], set()).add(word)
    count = 1
    for d in l:
        count *= len(d)
    ans = []
    word_set = set(words)
    for d in l:
        cur_count = count // len(d)
        for key, s in d.items():
            buf = word_set & s
            if len(buf) < cur_count:
                count = cur_count
                word_set = buf
                ans.append(key)
                break
    return ''.join(ans) if ans else '-'


T = int(input())
for t in range(T):
    N, L = input().split()
    N, L = int(N), int(L)
    words = []
    for i in range(N):
        words.append(input())
    answer = solution(N, L, words)
    print('Case #' + str(t+1) + ': ' + answer + '\n')
