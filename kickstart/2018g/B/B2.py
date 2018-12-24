# wrong answer, not finished yet
import math


def build_tree(boundaries, seg_tree, root, r, depth, offset):
    if depth == 0:
        seg_tree[root] += 1
    else:
        seg_tree[root] += r[1] - r[0] + 1
        pivot = int((root - offset) / 2)
        boundary_idx = pivot + int(offset / 2)
        dist = 2 ** depth - 1
        if int((root+dist)/2) < len(boundaries) and r[0] == boundaries[int((root-dist)/2)] and r[1] == boundaries[int((root+dist)/2)]:
            pass
        elif boundary_idx >= len(boundaries) or r[1] <= boundaries[boundary_idx]:
            build_tree(boundaries, seg_tree, pivot + offset, r, depth - 1, offset)
        elif r[0] > boundaries[boundary_idx]:
            build_tree(boundaries, seg_tree, root + pivot + 1, r, depth - 1, offset + 2 ** depth)
        else:
            r1 = (r[0], boundaries[boundary_idx])
            r2 = (boundaries[boundary_idx + 1], r[1])
            build_tree(boundaries, seg_tree, pivot + offset, r1, depth - 1, offset)
            build_tree(boundaries, seg_tree, root + pivot + 1, r2, depth - 1, offset + 2 ** depth)


def search_tree(boundaries, seg_tree, root, depth, offset, k):
    if depth == 0:
        return boundaries[int(root / 2)]
    pivot = int((root - offset) / 2)
    if k <= seg_tree[pivot + offset]:
        return search_tree(boundaries, seg_tree, pivot + offset, depth - 1, offset, k)
    elif k > seg_tree[root] - seg_tree[root + pivot + 1]:
        k -= seg_tree[root] - seg_tree[root + pivot + 1]
        return search_tree(boundaries, seg_tree, root + pivot + 1, depth - 1, offset + 2 ** depth, k)
    else:
        boundary_idx = pivot + int(offset / 2)
        k -= seg_tree[pivot + offset]
        length = boundaries[boundary_idx + 1] - boundaries[boundary_idx] + 1
        count = seg_tree[root] - seg_tree[root + pivot + 1] - seg_tree[pivot + offset]
        return boundaries[boundary_idx] + int((k - 1) / (count / length))


def solution(n, q, l1, l2, l3):
    x1, x2 = l1[0], l1[1]
    y1, y2 = l2[0], l2[1]
    z1, z2 = l3[0], l3[1]
    lr_list = [(min(x1, y1) + 1, max(x1, y1) + 1), (min(x2, y2) + 1, max(x2, y2) + 1)]
    k_list = [z1+1, z2+1]
    if n == 1:
        lr_list.pop()
    if q == 1:
        k_list.pop()
    a1, a2, a3 = l1[2], l2[2], l3[2]
    b1, b2, b3 = l1[3], l2[3], l3[3]
    c1, c2, c3 = l1[4], l2[4], l3[4]
    m1, m2, m3 = l1[5], l2[5], l3[5]
    for i in range(2, n):
        x1, x2 = x2, (a1 * x2 + b1 * x1 + c1) % m1
        y1, y2 = y2, (a2 * y2 + b2 * y1 + c2) % m2
        lr_list.append((x2 + 1, y2 + 1) if x2 < y2 else (y2 + 1, x2 + 1))
    for i in range(2, q):
        z1, z2 = z2, (a3 * z2 + b3 * z1 + c3) % m3
        k_list.append(z2 + 1)
    boundaries = {boundary for r in lr_list for boundary in r}
    boundaries = list(boundaries)
    boundaries.sort()
    depth = math.ceil(math.log2(len(boundaries)))
    seg_tree = [0 for i in range((2 ** (depth + 1) - 1))]
    root = 2 ** depth - 1
    for r in lr_list:
        build_tree(boundaries, seg_tree, root, r, depth, 0)
    result = 0
    for i in range(len(k_list)):
        k = seg_tree[root] - k_list[i] + 1
        val = 0
        if k > 0:
            val = search_tree(boundaries, seg_tree, root, depth, 0, k)
        result += (i + 1) * val
    return result


inputFile = open('B-large-practice.in', 'r')
outputFile = open('B.out', 'w')
numOfTests = int(inputFile.readline())
for test in range(numOfTests):
    N, Q = tuple(map(lambda x: int(x), inputFile.readline().split()))
    data1 = list(map(lambda x: int(x), inputFile.readline().split()))
    data2 = list(map(lambda x: int(x), inputFile.readline().split()))
    data3 = list(map(lambda x: int(x), inputFile.readline().split()))
    answer = solution(N, Q, data1, data2, data3)
    outputFile.write('Case #' + str(test+1) + ': ' + str(answer) + '\n')
    print(test)
inputFile.close()
outputFile.close()
