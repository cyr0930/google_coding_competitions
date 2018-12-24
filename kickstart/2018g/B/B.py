import math


def build_tree(bst_list, boundaries, root, r, depth, offset):
    if depth == 0:
        bst_list[root][0] += 1
    else:
        bst_list[root][0] += r[1] - r[0] + 1
        pivot = int((root - offset) / 2)
        boundary_idx = pivot + int(offset / 2)
        if boundary_idx >= len(boundaries) or r[1] <= boundaries[boundary_idx]:
            bst_list[root][1].append((pivot + offset, r, depth - 1, offset))
        elif r[0] > boundaries[boundary_idx]:
            bst_list[root][1].append((root + pivot + 1, r, depth - 1, offset + 2 ** depth))
        else:
            r1 = (r[0], boundaries[boundary_idx])
            r2 = (boundaries[boundary_idx + 1], r[1])
            bst_list[root][1].append((pivot + offset, r1, depth - 1, offset))
            bst_list[root][1].append((root + pivot + 1, r2, depth - 1, offset + 2 ** depth))


def solution(n, q, l1, l2, l3):
    x_list = [l1[0], l1[1]]
    y_list = [l2[0], l2[1]]
    z_list = [l3[0], l3[1]]
    lr_list = [(min(x_list[0], y_list[0]) + 1, max(x_list[0], y_list[0]) + 1), (min(x_list[1], y_list[1]) + 1, max(x_list[1], y_list[1]) + 1)]
    k_list = [z_list[0]+1, z_list[1]+1]
    if n == 1:
        lr_list.pop()
    if q == 1:
        k_list.pop()
    for i in range(2, n):
        x_list[0], x_list[1] = x_list[1], (l1[2]*x_list[1] + l1[3]*x_list[0] + l1[4]) % l1[5]
        y_list[0], y_list[1] = y_list[1], (l2[2]*y_list[1] + l2[3]*y_list[0] + l2[4]) % l2[5]
        lr_list.append((min(x_list[1], y_list[1]) + 1, max(x_list[1], y_list[1]) + 1))
    for i in range(2, q):
        z_list[0], z_list[1] = z_list[1], (l3[2]*z_list[1] + l3[3]*z_list[0] + l3[4]) % l3[5]
        k_list.append(z_list[1] + 1)
    boundaries = set()
    for r in lr_list:
        boundaries.add(r[0])
        boundaries.add(r[1])
    boundaries = list(boundaries)
    boundaries.sort()
    depth = math.ceil(math.log2(len(boundaries)))
    bst_list = [[0, []] for i in range((2 ** (depth + 1) - 1))]
    root = 2 ** depth - 1
    for r in lr_list:
        build_tree(bst_list, boundaries, root, r, depth, 0)
    result = 0
    for i in range(len(k_list)):
        k = bst_list[root][0] - k_list[i] + 1
        val = 0
        if k > 0:
            cur_root = root
            cur_offset = 0
            cur_depth = depth
            while cur_depth > 0:
                pivot = int((cur_root - cur_offset) / 2)
                while len(bst_list[cur_root][1]) > 0:
                    params = bst_list[cur_root][1].pop()
                    build_tree(bst_list, boundaries, *params)
                if k <= bst_list[pivot + cur_offset][0]:
                    cur_root = pivot + cur_offset
                elif k > bst_list[cur_root][0] - bst_list[cur_root + pivot + 1][0]:
                    k -= bst_list[cur_root][0] - bst_list[cur_root + pivot + 1][0]
                    cur_root = cur_root + pivot + 1
                    cur_offset = cur_offset + 2 ** cur_depth
                else:
                    k -= bst_list[pivot + cur_offset][0]
                    boundary_idx = pivot + int(cur_offset / 2)
                    length = boundaries[boundary_idx + 1] - boundaries[boundary_idx] - 1
                    count = bst_list[cur_root][0] - bst_list[cur_root + pivot + 1][0] - bst_list[pivot + cur_offset][0]
                    val = boundaries[boundary_idx] + 1 + int((k - 1) / (count / length))
                    break
                cur_depth -= 1
            val = boundaries[int((cur_root - cur_offset) / 2) + int(cur_offset / 2)] if val == 0 else val
        result += (i + 1) * val
    return result


inputFile = open('B-small-practice.in', 'r')
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
