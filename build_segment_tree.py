def build_segment_tree(arr, segmenttree, start, end, index):
    if start == end:
        segmenttree[index] = arr[start]
        return
    mid = (start + end) // 2
    build_segment_tree(arr, segmenttree, start, mid, 2 * index + 1)
    build_segment_tree(arr, segmenttree, mid + 1, end, 2 * index + 2)
    segmenttree[index] = segmenttree[2 * index + 1] + segmenttree[2 * index + 2]


arr = [1, 2, 3, 4]
segmenttree = [0] * (2 * len(arr))
build_segment_tree(arr, segmenttree, 0, len(arr) - 1, 0)
print(segmenttree)
