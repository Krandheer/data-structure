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
    if left > end or right < start:
        return 0
    if left >= start and end >= right:
        return segmenttree[index]

    mid = (left + right) // 2
    left = query_sum(start, end, 2 * index + 1, left, mid, segmenttree)
    right = query_sum(start, end, 2 * index + 2, mid + 1, right, segmenttree)
    return left + right


arr = [1, 2, 3, 4]
segmenttree = [0] * (2 * len(arr))
build_segment_tree(0, 0, len(arr) - 1, arr, segmenttree)
result = query_sum(1, 3, 0, 0, len(arr) - 1, segmenttree)
print(result)
