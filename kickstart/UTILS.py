def bin_search(l, k):
    start = 0
    end = len(l) - 1
    while start <= end:
        mid = start + int((end - start) / 2)
        if l[mid] <= k:
            start = mid + 1
        else:
            end = mid - 1
    return end


class Tree:
    def __init__(self, val):
        self.val = val
        self.frac = val[0] / val[1]
        self.count = 1
        self.left = None
        self.right = None

    def insert(self, val):
        self.count += 1
        frac = val[0] / val[1]
        if self.frac > frac:
            if self.left is None:
                self.left = Tree(val)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = Tree(val)
            else:
                self.right.insert(val)
