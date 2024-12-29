from typing import List


def build_segment_tree(index, left, right, arr, segmenttree):
    if left == right:
        segmenttree[index] = arr[left]
        return

    mid = (left + right) // 2

    build_segment_tree(2 * index + 1, left, mid, arr, segmenttree)
    build_segment_tree(2 * index + 2, mid + 1, right, arr, segmenttree)

    # build parent node
    segmenttree[index] = segmenttree[2 * index + 1] + segmenttree[2 * index + 2]


def query_sum(start, end, index, left, right, segmenttree):
    if end < left or start > right:
        return 0

    # this is basically saying range left-right is inside start-end
    if start <= left and right <= end:
        return segmenttree[index]

    mid = (left + right) // 2
    left = query_sum(start, end, 2 * index + 1, left, mid, segmenttree)
    right = query_sum(start, end, 2 * index + 2, mid + 1, right, segmenttree)
    return left + right


def update(index, val, i, l, r, segmenttree):
    if l == r:
        segmenttree[i] = val
        return
    mid = (l + r) // 2
    if i <= mid:
        update(index, val, 2 * i + 1, l, mid, segmenttree)
    else:
        update(index, val, 2 * i + 2, mid + 1, r, segmenttree)
    segmenttree[i] = segmenttree[2 * i + 1] + segmenttree[2 * i + 2]


arr = [1, 2, 3, 4]
segmenttree = [0] * (2 * len(arr))
build_segment_tree(0, 0, len(arr) - 1, arr, segmenttree)
result = query_sum(0, 2, 0, 0, len(arr) - 1, segmenttree)
print(result)
print(segmenttree)
update(1, 5, 0, 0, len(arr) - 1, segmenttree)
print(segmenttree)
