import math


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
    bst_count = [0 for i in range((2 ** (depth + 1) - 1))]
    bst_buffer = [[] for i in range((2 ** (depth + 1) - 1))]
    root = 2 ** depth - 1
    for r in lr_list:
        if depth == 0:
            bst_count[root] += 1
        else:
            bst_count[root] += r[1] - r[0] + 1
            sub_pivot = int(root / 2)
            if sub_pivot >= len(boundaries) or r[1] <= boundaries[sub_pivot]:
                bst_buffer[root].append((sub_pivot, r, depth - 1, 0))
            elif r[0] > boundaries[sub_pivot]:
                bst_buffer[root].append((root + sub_pivot + 1, r, depth - 1, 2 ** depth))
            else:
                r1 = (r[0], boundaries[sub_pivot])
                r2 = (boundaries[sub_pivot + 1], r[1])
                bst_buffer[root].append((sub_pivot, r1, depth - 1, 0))
                bst_buffer[root].append((root + sub_pivot + 1, r2, depth - 1, 2 ** depth))
    result = 0
    for i in range(len(k_list)):
        k = bst_count[root] - k_list[i] + 1
        val = 0
        if k > 0:
            cur_root = root
            cur_offset = 0
            cur_depth = depth
            while cur_depth > 0:
                pivot = int((cur_root - cur_offset) / 2)
                while len(bst_buffer[cur_root]) > 0:
                    sub_root, sub_r, sub_depth, sub_offset = bst_buffer[cur_root].pop()
                    if sub_depth == 0:
                        bst_count[sub_root] += 1
                    else:
                        bst_count[sub_root] += sub_r[1] - sub_r[0] + 1
                        sub_pivot = int((sub_root - sub_offset) / 2)
                        boundary_idx = sub_pivot + int(sub_offset / 2)
                        if boundary_idx >= len(boundaries) or sub_r[1] <= boundaries[boundary_idx]:
                            bst_buffer[sub_root].append((sub_pivot + sub_offset, sub_r, sub_depth - 1, sub_offset))
                        elif sub_r[0] > boundaries[boundary_idx]:
                            bst_buffer[sub_root].append((sub_root+sub_pivot+1, sub_r, sub_depth-1, sub_offset+2**sub_depth))
                        else:
                            r1 = (sub_r[0], boundaries[boundary_idx])
                            r2 = (boundaries[boundary_idx + 1], sub_r[1])
                            bst_buffer[sub_root].append((sub_pivot + sub_offset, r1, sub_depth - 1, sub_offset))
                            bst_buffer[sub_root].append((sub_root+sub_pivot+1, r2, sub_depth-1, sub_offset+2**sub_depth))
                if k <= bst_count[pivot + cur_offset]:
                    cur_root = pivot + cur_offset
                elif k > bst_count[cur_root] - bst_count[cur_root + pivot + 1]:
                    k -= bst_count[cur_root] - bst_count[cur_root + pivot + 1]
                    cur_root = cur_root + pivot + 1
                    cur_offset = cur_offset + 2 ** cur_depth
                else:
                    k -= bst_count[pivot + cur_offset]
                    boundary_idx = pivot + int(cur_offset / 2)
                    length = boundaries[boundary_idx + 1] - boundaries[boundary_idx] - 1
                    count = bst_count[cur_root] - bst_count[cur_root + pivot + 1] - bst_count[pivot + cur_offset]
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
