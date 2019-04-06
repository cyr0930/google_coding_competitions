def main():
    def make_case(div, n):
        case = []
        c = False
        for i in range(n):
            if i % div == 0:
                c = not c
            case.append('0' if c else '1')
        return case
    T = int(input())
    for t in range(T):
        N, B, F = input().split()
        N, B, F = int(N), int(B), int(F)
        div = 16
        room = None
        for i in range(F):
            case = make_case(div, N)
            print(''.join(case), flush=True)
            result = input()
            buf = []
            if room is None:
                count = 0
                cur = '0'
                for c in result:
                    if c != cur:
                        buf.append(div - count)
                        count = 0
                        cur = '0' if cur == '1' else '1'
                    count += 1
                buf.append((N % div) - count)
            else:
                offset = 0
                for count in room:
                    a, b = 0, 0
                    for j in range(count):
                        if result[offset + j] == '0':
                            a += 1
                        else:
                            b += 1
                    buf.append(a)
                    buf.append(b)
                    offset += count
            div = div // 2
            room = buf
        ans = []
        for i, val in enumerate(room):
            if val == 1:
                ans.append(str(i))
        print(' '.join(ans), flush=True)
        verdict = input()
        if verdict == '-1':
            break


if __name__ == '__main__':
    main()
