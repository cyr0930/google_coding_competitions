class Tree(object):
    def __init__(self, r, count=1):
        self.start = r[0]
        self.end = r[1]
        self.count = count
        self.totalCount = count * (r[1] - r[0] + 1)
        self.left = None
        self.right = None
        
    def insert(self, r, count=1):
        l = [(self, r, count)]
        while l:
            cur, r, count = l.pop()
            cur.totalCount += (r[1] - r[0] + 1) * count
            if r[1] < cur.start:
                if cur.left is None:
                    cur.left = Tree(r, count)
                else:
                    l.append((cur.left, r, count))
            elif cur.end < r[0]:
                if cur.right is None:
                    cur.right = Tree(r, count)
                else:
                    l.append((cur.right, r, count))
            elif r[0] <= cur.start and r[1] <= cur.end:
                if cur.end != r[1]:
                    if cur.right is None:
                        cur.right = Tree((r[1]+1, cur.end), cur.count)
                    else:
                        l.append((cur.right, (r[1]+1, cur.end), cur.count))
                if r[0] != cur.start:
                    if cur.left is None:
                        cur.left = Tree((r[0], cur.start-1), count)
                    else:
                        l.append((cur.left, (r[0], cur.start-1), count))
                cur.end = r[1]
                cur.count += count
            elif cur.start <= r[0] and cur.end <= r[1]:
                if r[0] != cur.start:
                    if cur.left is None:
                        cur.left = Tree((cur.start, r[0]-1), cur.count)
                    else:
                        l.append((cur.left, (cur.start, r[0]-1), cur.count))
                if cur.end != r[1]:
                    if cur.right is None:
                        cur.right = Tree((cur.end+1, r[1]), count)
                    else:
                        l.append((cur.right, (cur.end+1, r[1]), count))
                cur.start = r[0]
                cur.count += count
            elif cur.start < r[0] and r[1] < cur.end:
                if cur.left is None:
                    cur.left = Tree((cur.start, r[0]-1), cur.count)
                else:
                    l.append((cur.left, (cur.start, r[0]-1), cur.count))
                if cur.right is None:
                    cur.right = Tree((r[1]+1, cur.end), cur.count)
                else:
                    l.append((cur.right, (r[1]+1, cur.end), cur.count))
                cur.start = r[0]
                cur.end = r[1]
                cur.count += count
            else:   # r[0] < cur.start and cur.end < r[1]
                if cur.left is None:
                    cur.left = Tree((r[0], cur.start - 1), count)
                else:
                    l.append((cur.left, (r[0], cur.start - 1), count))
                if cur.right is None:
                    cur.right = Tree((cur.end + 1, r[1]), count)
                else:
                    l.append((cur.right, (cur.end + 1, r[1]), count))
                cur.count += count

    def search(self, k):
        if k > self.totalCount:
            return 0
        left_count = 0 if self.left is None else self.left.totalCount
        right_count = 0 if self.right is None else self.right.totalCount
        if right_count >= k:
            return self.right.search(k)
        elif self.totalCount - left_count < k:
            return self.left.search(k - self.totalCount + left_count)
        else:
            return self.end - int((k-right_count-1)/self.count)


def solution(n, q, l1, l2, l3):
    x_list = [l1[0], l1[1]]
    y_list = [l2[0], l2[1]]
    z_list = [l3[0], l3[1]]
    lr_list = [(min(x_list[0], y_list[0]) + 1, max(x_list[0], y_list[0]) + 1), (min(x_list[1], y_list[1]) + 1, max(x_list[1], y_list[1]) + 1)]
    k_list = [z_list[0]+1, z_list[1]+1]
    for i in range(2, n):
        x_list[0], x_list[1] = x_list[1], (l1[2]*x_list[1] + l1[3]*x_list[0] + l1[4]) % l1[5]
        y_list[0], y_list[1] = y_list[1], (l2[2]*y_list[1] + l2[3]*y_list[0] + l2[4]) % l2[5]
        lr_list.append((min(x_list[1], y_list[1]) + 1, max(x_list[1], y_list[1]) + 1))
    for i in range(2, q):
        z_list[0], z_list[1] = z_list[1], (l3[2]*z_list[1] + l3[3]*z_list[0] + l3[4]) % l3[5]
        k_list.append(z_list[1] + 1)
    lr_list = lr_list[:n]
    k_list = k_list[:q]
    # t = Tree(lr_list.pop())
    # for i in range(len(lr_list)):
    #     t.insert(lr_list[i])
    # result = 0
    # for i in range(len(k_list)):
    #     result += t.search(k_list[i]) * (i+1)
    lr_list.sort()
    boundary = set()
    for i in range(len(lr_list)):
        boundary.add((lr_list[i][0], False))
        boundary.add((lr_list[i][1], True))
    boundary = list(boundary)
    boundary.sort()
    dictionary = {}
    idx = 1
    lparen = boundary[0][0]
    while True:
        if boundary[idx][1]:
            dictionary[(lparen, boundary[idx][0])] = 0
            if idx == len(boundary)-1:
                break
            lparen = boundary[idx][0] + 1
            idx += 2 if not boundary[idx+1][1] and boundary[idx+1][0] == boundary[idx][0] + 1 else 1
        else:
            dictionary[(lparen, boundary[idx][0]-1)] = 0
            lparen = boundary[idx][0]
            idx += 1
    keys = list(dictionary.keys())
    start = 0
    for r in lr_list:
        while r[0] > keys[start][0]:
            start += 1
        for i in range(start, len(keys)):
            if r[0] <= keys[i][0] and keys[i][1] <= r[1]:
                dictionary[keys[i]] += 1
            else:
                break
    return 0


inputFile = open('B-small-practice.in', 'r')
outputFile = open('B.out', 'w')
numOfTests = int(inputFile.readline())
for test in range(numOfTests):
    print(test)
    N, Q = tuple(map(lambda x: int(x), inputFile.readline().split()))
    data1 = list(map(lambda x: int(x), inputFile.readline().split()))
    data2 = list(map(lambda x: int(x), inputFile.readline().split()))
    data3 = list(map(lambda x: int(x), inputFile.readline().split()))
    answer = solution(N, Q, data1, data2, data3)
    outputFile.write('Case #' + str(test+1) + ': ' + str(answer) + '\n')
inputFile.close()
outputFile.close()
