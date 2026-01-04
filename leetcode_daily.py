import bisect
from curses.ascii import isalnum
from functools import lru_cache
import heapq
from collections import Counter, defaultdict, deque
import math
from re import I
from typing import List


def find_minimumTime(strength: List[int], K: int) -> int:
    x = 1
    energy = 0
    time = 0
    n = len(strength)
    strength.sort()
    i = 0
    temp = defaultdict(int)
    for ele in strength:
        temp[ele] += 1
    while n > 0:
        time += 1
        energy = energy + x

        if energy >= strength[i]:
            n = n - 1
            energy = 0
            x = x + K
            temp[strength[i]] -= 1
            i += 1
        elif energy in temp and temp[energy] > 0:
            n = n - 1
            x = x + K
            temp[energy] -= 1
            energy = 0
            i += 1

    return time


# print(find_minimumTime([20, 22, 16], 10))


def max_two_events(events: List[List[int]]):
    events.sort(key=lambda x: x[0])
    memo = {}

    def dp(index, prev_end, k):
        if index >= len(events):
            return 0

        if (index, prev_end) in memo:
            return memo[(index, prev_end)]

        start, end, val = events[index]
        not_take = dp(index + 1, prev_end, k)
        take = 0
        if start > prev_end and k < 2:
            take = val + dp(index + 1, end, k + 1)
        result = max(take, not_take)
        memo[(index, prev_end)] = result
        return result

    return dp(0, float("-inf"), 0)

    # print(max_two_events([[1, 3, 2], [4, 5, 2], [1, 5, 5]]))


def is_array_special(nums: List[int], queries: List[List[int]]) -> List[bool]:
    def found(start, end, voilating_index):
        left, right = 0, len(voilating_index) - 1
        while left <= right:
            mid = (left + right) // 2
            index = voilating_index[mid]
            if start < index <= end:
                return True
            elif index < start:
                left = mid + 1
            else:
                right = mid - 1
        return False

    voilating_index = []
    for i in range(1, len(nums)):
        if nums[i - 1] % 2 == nums[i] % 2:
            voilating_index.append(i)
    ans = []
    for q in queries:
        start, end = q
        if found(start, end, voilating_index):
            ans.append(False)
        else:
            ans.append(True)
    return ans


# print(is_array_special([4, 3, 1, 6], [[0, 2], [2, 3]]))


def pick_gifts(gifts: List[int], k: int) -> int:
    temp = [-num for num in gifts]
    heapq.heapify(temp)
    for _ in range(k):
        heapq.heappush(temp, -(math.isqrt(-heapq.heappop(temp))))
    return sum([-x for x in temp])


# print(pick_gifts([25, 64, 9, 4, 100], 4))


def find_score(nums: List[int]) -> int:
    marked = [False] * len(nums)
    ans = 0
    heap = []
    for i, num in enumerate(nums):
        heapq.heappush(heap, (num, i))
    while heap:
        num, i = heapq.heappop(heap)
        if not marked[i]:
            ans += num
            marked[i] = True
            if i - 1 >= 0:
                marked[i - 1] = True
            if i + 1 < len(nums):
                marked[i + 1] = True
    return ans


def continuous_subarrays(nums: List[int]) -> int:
    left, right, count = 0, 0, 0
    n = len(nums)
    temp = {}
    while right < n:
        temp[nums[right]] = temp.get(nums[right], 0) + 1
        while max(temp) - min(temp) > 2:
            temp[nums[left]] -= 1
            if temp[nums[left]] == 0:
                del temp[nums[left]]
            left += 1
        count += right - left + 1
        right += 1

    return count


# print(continuous_subarrays([5, 4, 2, 4]))


def max_average_ratio(classes: List[List[int]], extra_students: int) -> float:
    # leetcode 1792. Maximum Average Pass Ratio
    heap = []
    for i, val in enumerate(classes):
        a, b = val
        j = (a / b) - (a + 1) / (b + 1)
        heapq.heappush(heap, (j, i))

    while extra_students > 0:
        j, i = heapq.heappop(heap)
        a, b = classes[i]
        classes[i] = [a + 1, b + 1]
        j = ((a + 1) / (b + 1)) - ((a + 2) / (b + 2))
        heapq.heappush(heap, (j, i))
        extra_students -= 1

    res = 0
    for i, val in enumerate(classes):
        a, b = val
        res += a / b
    return res / len(classes)


# print(max_average_ratio([[1, 2], [3, 5], [2, 2]], 2))


def get_final_state(nums: List[int], k: int, multiplier: int) -> List[int]:
    heap = []
    for index, num in enumerate(nums):
        heapq.heappush(heap, (num, index))

    while k > 0:
        num, i = heapq.heappop(heap)
        num = num * multiplier
        nums[i] = num
        heapq.heappush(heap, (num, i))
        k -= 1
    return nums


# print(get_final_state([2, 1, 3, 5, 6], 5, 2))


def repeat_limited_string(s: str, repeat_limit: int) -> str:
    freq = defaultdict(int)
    for char in s:
        freq[char] += 1
    heap = []
    for k in freq:
        heapq.heappush(heap, (-ord(k), k))

    res = []
    while heap:
        _, char = heapq.heappop(heap)
        count = freq[char]
        curr_count = min(count, repeat_limit)
        res.append(char * curr_count)
        if count - curr_count > 0 and heap:
            _, next_char = heapq.heappop(heap)
            next_count = freq[next_char]
            res.append(next_char)
            if next_count > 1:
                freq[next_char] -= 1
                heapq.heappush(heap, (-ord(next_char), next_char))
            heapq.heappush(heap, (-ord(char), char))
            freq[char] -= curr_count

    return "".join(res)


# print(repeat_limited_string("cczazcc", 3))


def final_prices(prices: List[int]) -> List[int]:
    ans = []
    for i, price in enumerate(prices):
        discount = 0
        for j in range(i + 1, len(prices)):
            if prices[j] <= price:
                discount = prices[j]
                break
        ans.append(price - discount)
    return ans


# print(final_prices([8, 4, 6, 2, 3]))


def max_chunks_to_sorted(arr: List[int]) -> int:
    res = 0
    curr_max = -1
    for i, num in enumerate(arr):
        # this works because all elements are distinct, so if max value == index
        # that means all other values till that index will have values from
        # 0...index
        curr_max = max(curr_max, num)
        if curr_max == i:
            res += 1
    return res


def max_k_divisible_components(
    edges: List[List[int]], values: List[int], k: int
) -> int:
    # greedy approach to maximize connected component. start from bottom, leaf node,
    # if it is divisible by k then it is one component otherwise it passes up it's value to parent and then
    # if sum at parent is divisible by k then it becomes one separate component.

    adj = defaultdict(list)

    for n1, n2 in edges:
        adj[n1].append(n2)
        adj[n2].append(n1)

    res = 0

    def dfs(curr_node, parent):
        total = values[curr_node]
        for node in adj[curr_node]:
            if node != parent:
                total += dfs(node, curr_node)
        if total % k == 0:
            nonlocal res
            res += 1
        return total

    dfs(0, -1)

    return res


def leftmost_building_queries(
    heights: List[int], queries: List[List[int]]
) -> List[int]:
    ans = [-1] * len(queries)
    groups = defaultdict(list)
    for i, q in enumerate(queries):
        l, r = sorted(q)
        if l == r or heights[r] > heights[l]:
            ans[i] = r
        else:
            maxi = max(heights[l], heights[r])
            groups[r].append((maxi, i))

    min_heap = []
    for i, h in enumerate(heights):
        for q_h, q_i in groups[i]:
            heapq.heappush(min_heap, (q_h, q_i))
        while min_heap and h > min_heap[0][0]:
            q_h, q_i = heapq.heappop(min_heap)
            ans[q_i] = i

    return ans


# this one gives tle but very good solution of thinking track of graph. as you think of recursive tree of take not take.
# this is actually quite simple and elegant solution but only problem is it is slow.
def find_target_sum_ways(nums: List[int], target: int) -> int:
    ans = deque()
    for num in nums:
        if not ans:
            ans.append(-num)
            ans.append(num)
            continue
        for _ in range(len(ans)):
            t = ans.popleft()
            ans.append(t + num)
            ans.append(t - num)
    count = 0
    for _ in range(len(ans)):
        elem = ans.popleft()
        if elem == target:
            count += 1
    return count


# tag: dp
def recur(nums, i, current_sum, target, dp):
    if i == len(nums):
        return 1 if current_sum == target else 0
    key = (i, current_sum)
    if key in dp:
        return dp[key]
    plus = recur(nums, i + 1, current_sum + nums[i], target, dp)
    minus = recur(nums, i + 1, current_sum - nums[i], target, dp)
    dp[key] = plus + minus
    return dp[key]


# nums = [1, 0]
# target = 1
# dp = {}
# print(recur(nums, 0, 0, target, dp))


def maxScore(s: str):
    left = defaultdict(int)
    num_zeroes = 0
    for i, ch in enumerate(s):
        if ch == "0":
            num_zeroes += 1
        left[i] = num_zeroes
    num_ones = 0
    right = defaultdict(int)
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "1":
            num_ones += 1
        right[i] = num_ones

    maxi = float("-inf")
    for i in range(len(s)):
        temp = left[i] + right[i]
        maxi = max(temp, maxi)
    return maxi


def vowelStrings(words: List[str], queries: List[List[int]]) -> List[int]:
    temp = []
    for w in words:
        if w[0] in "aeiou" and w[-1] in "aeiou":
            temp.append(1)
        else:
            temp.append(0)

    pref = [0] * len(temp)
    pref[0] = temp[0]
    for i in range(1, len(temp)):
        pref[i] = pref[i - 1] + temp[i]
    ans = []
    for l, r in queries:
        if l == 0:
            ans.append(pref[r])
        else:
            ans.append(pref[r] - pref[l - 1])
    return ans


# words = ["aba", "bcb", "ece", "aa", "e"]
# queries = [[0, 2], [1, 4], [1, 1]]
# vowelStrings(words, queries)


def ways_to_split_array(nums: List[int]) -> int:
    n = len(nums)
    pref = [0] * n
    pref[0] = nums[0]

    for i in range(1, n):
        pref[i] = pref[i - 1] + nums[i]

    count = 0

    for i in range(n - 1):
        first = pref[i]
        last = pref[-1] - pref[i]
        if first >= last:
            count += 1

    return count


def ways_to_split_array2(nums: List[int]) -> int:
    count = 0
    n = len(nums)
    temp_sum = sum(nums)
    first = 0
    for i in range(n - 1):
        first += nums[i]
        last = temp_sum - first
        if first >= last:
            count += 1

    return count


# print(ways_to_split_array([2, 3, 1, 0]))


def countPalindromicSubsequence(s: str) -> int:
    # key point is that for 3 letter pallindrom if first and last are same then
    # everything in between will form palindrome, just need to makes sure that same
    # palindrome is not counted for that use seen in that range.

    freq = Counter(s)

    considered = {}

    for ch, count in freq.items():
        if count >= 2:
            considered[ch] = True

    matters = defaultdict(list)

    for index, ch in enumerate(s):
        if ch in considered:
            matters[ch].append(index)

    count = 0

    for k, v in matters.items():
        left, right = v[0], v[-1]
        temp = set()
        for i in range(left + 1, right):
            temp.add(s[i])
        count += len(temp)
    return count


# tag: prefix_sum, revise.
def shiftingLetters(s: str, shifts: List[List[int]]) -> str:
    prefix = [0] * (len(s) + 1)
    for u, v, w in shifts:
        if w == 1:
            prefix[u] += -1
            prefix[v + 1] += 1
        else:
            prefix[u] += 1
            prefix[v + 1] += -1

    diff = 0
    res = [ord(c) - ord("a") for c in s]
    for i in reversed(range(len(s) + 1)):
        diff += prefix[i]
        res[i - 1] = (res[i - 1] + diff) % 26
    s1 = [chr(ord("a") + n) for n in res]
    return "".join(s1)


def minOperations(boxes: str) -> List[int]:
    n = len(boxes)
    ans = [0] * n
    for i in range(n):
        temp = 0
        for j in range(n):
            if boxes[j] == "1":
                temp += abs(j - i)
        ans[i] = temp
    return ans


def stringMatching(words: List[str]) -> List[str]:
    ans = []
    for i, word in enumerate(words):
        for j, cmp in enumerate(words):
            if i == j:
                continue
            if word in cmp:
                ans.append(word)
                break

    return ans


def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    def get_freq(word):
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord("a")] += 1
        return freq

    max_freq = [0] * 26
    for word in words2:
        curr_freq = get_freq(word)
        for i in range(26):
            max_freq[i] = max(max_freq[i], curr_freq[i])

    ans = []
    for word in words1:
        freq = get_freq(word)
        if all(freq[i] >= max_freq[i] for i in range(26)):
            ans.append(word)

    return ans


# words1 = ["cccbb", "aacbc", "bbccc", "baaba", "acaba"]
# words2 = ["cb", "b", "cb"]
# print(wordSubsets(words1, words2))


def canConstruct(s: str, k: int) -> bool:
    if k > len(s):
        return False

    freq = defaultdict(int)
    for i in s:
        freq[i] += 1

    odd_count = 0

    for i, v in freq.items():
        if v & 1:
            odd_count += 1

    if odd_count > k:
        return False

    return True


def canBeValid(s: str, locked: str) -> bool:
    if len(s) & 1:
        return False
    wildcard = []
    stack = []
    n = len(s)
    for i in range(n):
        if locked[i] == "0":
            wildcard.append(i)
        elif s[i] == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            elif wildcard:
                wildcard.pop()
            else:
                return False
    while stack and wildcard and stack[-1] < wildcard[-1]:
        stack.pop()
        wildcard.pop()

    if stack:
        return False

    return False if len(wildcard) & 1 else True


def minimumLength(s: str) -> int:
    temp = defaultdict(int)
    for i in s:
        temp[i] += 1
    ans = 0
    for v in temp.values():
        if v <= 2:
            ans += v
        elif v & 1:
            ans += 1
        else:
            ans += 2
    return ans


def findThePrefixCommonArray(A: List[int], B: List[int]) -> List[int]:
    common_a = set()
    common_b = set()
    n = len(A)
    n = len(A)
    pre = [0] * n
    for i in range(n):
        common_a.add(A[i])
        common_b.add(B[i])
        temp = common_a.intersection(common_b)
        pre[i] = len(temp)
    return pre


def doesValidArrayExist(derived: List[int]) -> bool:
    # if derived array comes from original array then the xor of derived array
    # should we 0, why? because in derived array each element is xor of two element in that
    # way if we do xor sum of derived array then each element will appear twice, making it
    # equal to 0
    ans = 0
    for i in derived:
        ans ^= i
    return ans == 0


def minCost(grid: List[List[int]]):
    row, col = len(grid), len(grid[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    visited = []
    for _ in range(row):
        temp = []
        for _ in range(col):
            temp.append(False)
        visited.append(temp)

    def dfs(i, j, cost):
        if i == row - 1 and j == col - 1:
            return cost
        if visited[i][j]:
            return float("inf")
        min_cost = float("inf")
        visited[i][j] = True
        for index, val in enumerate(directions):
            dx, dy = i + val[0], j + val[1]
            if 0 <= dx < row and 0 <= dy < col:
                new_cost = cost + 1 if grid[i][j] != index + 1 else cost
                min_cost = min(min_cost, dfs(dx, dy, new_cost))
        visited[i][j] = False
        return min_cost

    return dfs(0, 0, 0)


def minCost2(grid: List[List[int]]):
    # tag: dijkshatra_algo, graph
    row, col = len(grid), len(grid[0])
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    distance = [[float("inf")] * col for _ in range(row)]
    visited = [[False] * col for _ in range(row)]

    def bfs(i, j, cost):
        q = []
        heapq.heappush(q, (cost, i, j))
        visited[i][j] = True

        while q:
            cost, x, y = heapq.heappop(q)
            for ind, v in enumerate(directions):
                dx, dy = x + v[0], y + v[1]
                if 0 <= dx < row and 0 <= dy < col:
                    new_cost = cost + 1 if ind + 1 != grid[x][y] else cost
                    if new_cost < distance[dx][dy]:
                        distance[dx][dy] = new_cost
                        heapq.heappush(q, (new_cost, dx, dy))
        return distance[row - 1][col - 1]

    return bfs(0, 0, 0)


def trapRainWater(heightMap: List[List[int]]) -> int:
    m, n = len(heightMap), len(heightMap[0])
    queue = []
    visited = [[False] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if i in [0, m - 1] or j in [0, n - 1]:
                heapq.heappush(queue, (heightMap[i][j], i, j))
                visited[i][j] = True
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    ans = 0
    while queue:
        height, x, y = heapq.heappop(queue)
        for u, v in direction:
            dx, dy = x + u, y + v

            if 0 <= dx < m and 0 <= dy < n and not visited[dx][dy]:
                ans += max(height - heightMap[dx][dy], 0)
                heapq.heappush(queue, (max(height, heightMap[dx][dy]), dx, dy))
                visited[dx][dy] = True
    return ans


def firstCompleteIndex(arr: List[int], mat: List[List[int]]):
    row, col = len(mat), len(mat[0])
    r_sum = []
    c_sum = []
    h_map = {}
    for r in range(row):
        temp = 0
        for c in range(col):
            temp += mat[r][c]
            h_map[mat[r][c]] = (r, c)
        r_sum.append(temp)

    for c in range(col):
        temp = 0
        for r in range(row):
            temp += mat[r][c]
        c_sum.append(temp)

    for index, elem in enumerate(arr):
        i, j = h_map[elem]
        temp1 = r_sum[i] - elem
        r_sum[i] = temp1
        temp2 = c_sum[j] - elem
        c_sum[j] = temp2
        if temp1 == 0 or temp2 == 0:
            return index


# tag: wow, amazing problem. lc 2017. gridGame, #grid
def gridGame(grid: List[List[int]]) -> float:
    top_sum = sum(grid[0])
    bottom_sum = 0
    mini = float("inf")
    for i in range(len(grid[0])):
        top_sum -= grid[0][i]
        mini = min(mini, max(top_sum, bottom_sum))
        bottom_sum += grid[1][i]
    return mini


# tags: bfs question, lc 1765. map of highest peak, problem description is so bad, I thought I will need to watch
# video to understand the solution and problem but reading some discussion section I got it and coded myself.
# it is basically multiple source bfs, start from water and then move to land.
# One good learning was that any multiple source bfs can be converted to single source bfs by adding all sources to
# a node and then start bfs from that node. and in end just subtract one from distance.
def highestPeak(isWater: List[List[int]]) -> List[List[int]]:
    m, n = len(isWater), len(isWater[0])
    q = deque()
    for i in range(m):
        for j in range(n):
            if isWater[i][j] == 1:
                q.append((i, j))

    heights = [[0 if cell == 1 else -1 for cell in row] for row in isWater]
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q:
        x, y = q.popleft()
        for u, v in directions:
            dx, dy = x + u, y + v
            if 0 <= dx < m and 0 <= dy < n and heights[dx][dy] == -1:
                heights[dx][dy] = heights[x][y] + 1
                q.append((dx, dy))

    return heights


def countServers(grid: List[List[int]]) -> int:
    m, n, connected = len(grid), len(grid[0]), 0
    rows, col = [0] * m, [0] * n

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                rows[i] += 1
                col[j] += 1

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1 and (rows[i] > 1 or col[j] > 1):
                connected += 1

    return connected


# tag: graph, cycle detection concept could be used
def eventualSafeNodes(graph: List[List[int]]) -> List[int]:
    n = len(graph)
    state = [0] * n

    def dfs(node):
        if state[node] > 0:
            return state[node] == 2
        state[node] = 1
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False
        state[node] = 2
        return True

    return [node for node in range(n) if dfs(node)]


# tag: quite interesting problem. observations is key
def lexicographicallySmallestArray(nums: List[int], limit: int) -> List[int]:
    groups = []
    num_group = {}

    for n in sorted(nums):
        if not groups or abs(n - groups[-1][-1]) > limit:
            groups.append(deque())
        groups[-1].append(n)
        num_group[n] = len(groups) - 1

    res = []
    for n in nums:
        j = num_group[n]
        res.append(groups[j].popleft())
    return res


# tags: probably the hardest leetcode problem ever.
def maximumInvitations(favorite: List[int]) -> int:
    n = len(favorite)
    longest_cycle = 0
    visited = [False] * n
    len_2_cycle = []

    for i in range(n):
        if visited[i]:
            continue
        start, curr = i, i
        curr_set = set()

        while not visited[curr]:
            visited[curr] = True
            curr_set.add(curr)
            curr = favorite[curr]

        if curr in curr_set:
            length = len(curr_set)
            while start != curr:
                length -= 1
                start = favorite[start]
            longest_cycle = max(longest_cycle, length)
            if length == 2:
                len_2_cycle.append((curr, favorite[curr]))

    inverted = defaultdict(list)
    for dest, src in enumerate(favorite):
        inverted[src].append(dest)

    def bfs(src, parent):
        q = deque()
        q.append((src, 0))
        max_length = 0

        while q:
            node, dest = q.popleft()
            if node == parent:
                continue
            max_length = max(max_length, dest)
            for nei in inverted[node]:
                q.append((nei, dest + 1))
        return max_length

    chain_sum = 0

    for n1, n2 in len_2_cycle:
        chain_sum += bfs(n1, n2) + bfs(n2, n1) + 2
    return max(chain_sum, longest_cycle)


def checkIfPrerequisite(
    numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
) -> List[bool]:
    # this could be optimised more using toposort kahn's algo but didn't had time to spend more on this problem so have not optimised yet
    adj = defaultdict(list)
    for u, v in prerequisites:
        adj[u].append(v)

    def dfs(graph, src, dest, visited):
        visited[src] = True
        if src == dest:
            return True

        isReachable = False
        for node in adj[src]:
            if not visited[node]:
                isReachable = isReachable or dfs(graph, node, dest, visited)
        return isReachable

    ans = []
    for u, v in queries:
        visited = [False] * numCourses
        ans.append(dfs(adj, u, v, visited))
    return ans


def magnificentSets(n: int, edges: List[List[int]]) -> int:
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def get_component(src):
        q = deque([(src, 1)])
        visit = {src: 1}
        while q:
            node, l = q.popleft()
            for nei in graph[node]:
                if nei in visit:
                    if visit[nei] == l:
                        return visit, -1
                    continue
                visit[nei] = l + 1
                q.append((nei, l + 1))
                visited.add(nei)
        return visit, max(visit.values())

    res = 0
    for i in range(1, n + 1):
        if i in visited:
            continue
        visited.add(i)
        component, length = get_component(i)
        if length == -1:
            return -1

        max_count = 0
        for src in component:
            _, maxi = get_component(src)
            max_count = max(max_count, maxi)
        res += max_count
    return res


# tag: nice intuitive solution, for rotated sorted array.
def check(nums: List[int]) -> bool:
    count = 0
    n = len(nums)

    for i in range(n):
        if nums[i] > nums[(i + 1) % n]:
            count += 1
        if count > 1:
            return False

    return True


def longestMonotonicSubarray(nums: List[int]) -> int:
    in_len, max_in_len = 1, 1
    de_len, max_de_len = 1, 1

    n = len(nums)
    for i in range(1, n):
        if nums[i - 1] < nums[i]:
            in_len += 1
        else:
            max_in_len = max(max_in_len, in_len)
            in_len = 1
    for i in range(1, n):
        if nums[i - 1] > nums[i]:
            de_len += 1
        else:
            max_de_len = max(max_de_len, de_len)
            de_len = 1
    max_in_len = max(max_in_len, in_len)
    max_de_len = max(max_de_len, de_len)

    return max(max_in_len, max_de_len)


def areAlmostEqual(s1, s2):
    i, j = -1, -1
    cnt = 0
    for k in range(0, len(s1)):
        if s1[k] != s2[k]:
            cnt += 1
            if i == -1:
                i = k
            elif j == -1:
                j = k

    if cnt == 0:
        return True
    elif cnt == 2 and s1[i] == s2[j] and s1[j] == s2[i]:
        return True

    return False


def tupleSameProduct(nums: List[int]) -> int:
    freq = defaultdict(int)
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            freq[nums[i] * nums[j]] += 1

    return sum(f * (f - 1) * 4 for f in freq.values())


def queryResults(limit: int, queries: List[List[int]]) -> List[int]:
    ans = []
    balls = defaultdict(int)
    color = defaultdict(int)
    for ball, c in queries:
        if ball in balls:
            temp = balls[ball]
            color[temp] -= 1
            if color[temp] == 0:
                del color[temp]
        balls[ball] = c
        color[c] += 1
        ans.append(len(color))

    return ans


def countBadPairs(nums: List[int]) -> int:
    # at each index the max bad pair is the index itself.
    # so we can keep track of how many good pairs we have seen so far
    # and then at each index we can calculate how many bad pairs we have seen so far
    # and then add that to our answer.
    bad_pairs = 0
    diff_count = defaultdict(int)
    for ind, num in enumerate(nums):
        diff = ind - num
        good_pairs_count = diff_count.get(diff, 0)
        bad_pairs += ind - good_pairs_count
        diff_count[diff] += 1

    return bad_pairs


def clearDigits(s: str) -> str:
    nearest_alpha = 0
    n = len(s)
    temp = [False] * n
    for i in range(n):
        if s[i].isalpha():
            nearest_alpha = i
        elif s[i].isdigit():
            temp[nearest_alpha] = True
            temp[i] = True
            while nearest_alpha > 0 and temp[nearest_alpha]:
                nearest_alpha -= 1
    return "".join(s[i] for i in range(n) if not temp[i])


def removeOccurrences(s: str, part: str) -> str:
    while part in s:
        start = s.index(part)
        s = s[:start] + s[start + len(part) :]
    return s


def minOperations_1(self, nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    ans = 0
    for i in range(len(nums)):
        x = heapq.heappop(nums)
        if x < k:
            y = heapq.heappop(nums)
            ans += 1
            temp = min(x, y) * 2 + max(x, y)
            heapq.heappush(nums, temp)
        else:
            break
    return ans


def punishmentNumber(n: int) -> int:
    def is_valid(start, curr_sum, target, string):
        if start == len(string) and curr_sum == target:
            return True
        for i in range(start, len(string)):
            if is_valid(i + 1, curr_sum + int(string[start : i + 1]), target, string):
                return True
        return False

    ans = 0
    for i in range(1, n + 1):
        if is_valid(0, 0, i, str(i * i)):
            ans += i * i

    return ans


def sumOfGoodNumbers(nums: List[int], k: int) -> int:
    n = len(nums)
    ans = 0
    for ind, num in enumerate(nums):
        left_exists = ind - k >= 0
        right_exists = ind + k < n
        if not left_exists and not right_exists:
            ans += num
        elif not left_exists and right_exists:
            if num > nums[ind + k]:
                ans += num
        elif not right_exists and left_exists:
            if num > nums[ind - k]:
                ans += num
        elif num > nums[ind - k] and num > nums[ind + k]:
            ans += num
    return ans


def solve(n, tiles, used, result, string):
    result.add(string)
    for i in range(n):
        if used[i]:
            continue
        used[i] = True
        solve(n, tiles, used, result, string + tiles[i])
        used[i] = False


def numTilePossibilities(tiles: str) -> int:
    n = len(tiles)
    used = defaultdict(bool)
    result = set()
    solve(n, tiles, used, result, "")
    return len(result) - 1


def smallestNumber(pattern: str):
    used = [False] * 10
    result = []

    def helper(curr_position, pattern):
        if curr_position == len(pattern) + 1:
            return True
        for i in range(1, 10):
            if used[i]:
                continue
            if curr_position > 0:
                if pattern[curr_position - 1] == "D" and result[-1] <= i:
                    continue
                if pattern[curr_position - 1] == "I" and result[-1] >= i:
                    continue

            used[i] = True
            result.append(i)
            if helper(curr_position + 1, pattern):
                return True
            result.pop()
            used[i] = False
        return False

    if helper(0, pattern):
        return "".join(str(i) for i in result)


def getHappyString(n: int, k: int):
    string = ["a", "b", "c"]
    result = []

    def helper(curr_string):
        if len(curr_string) == n:
            result.append(curr_string)
            return
        for s in string:
            if not curr_string or s != curr_string[-1]:
                helper(curr_string + s)

    helper("")
    if k > len(result):
        return ""
    return result[k - 1]


def findDifferentBinaryString(nums: List[str]):
    lookup = Counter(nums)
    n = len(nums)

    def helper(p):
        if len(p) == n and p not in lookup:
            return p
        if len(p) > n:
            return
        for i in range(n):
            for j in range(2):
                ans = helper(p + str(j))
                if ans:
                    return ans

    return helper("")


def numberOfSubstrings(s: str) -> int:
    track = defaultdict(int)
    ans = 0
    i, j = 0, 0
    while i <= j < len(s):
        track[s[j]] += 1
        while len(track) == 3:
            ans += len(s) - j
            track[s[i]] -= 1
            if track[s[i]] == 0:
                del track[s[i]]
            i += 1
        j += 1
    return ans


def minZeroArray(nums: List[int], queries: List[List[int]]) -> int:
    n = len(nums)
    total_sum = 0
    k = 0
    difference_array = [0] * (n + 1)

    for index in range(n):
        while total_sum + difference_array[index] < nums[index]:
            k += 1
            if k > len(queries):
                return -1
            left, right, val = queries[k - 1]
            if right >= index:
                difference_array[max(left, index)] += val
                difference_array[right + 1] -= val
        total_sum += difference_array[index]

    return k


def maximumCandies(candies: List[int], k: int) -> int:
    def is_possible(mid):
        max_children = 0
        for candy in candies:
            max_children += candy // mid
        return max_children >= k

    left, right = 0, max(candies)
    while left < right:
        mid = (left + right + 1) // 2
        if is_possible(mid):
            left = mid
        else:
            right = mid - 1
    return left


def minCapability(self, nums: List[int], k: int) -> int:
    left, right = min(nums), max(nums)

    def canPick(mid):
        """Check if we can pick k elements where max value ≤ mid."""
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] <= mid:
                count += 1
                i += 1
            i += 1
        return count >= k

    while left < right:
        mid = (left + right) // 2
        if canPick(mid):
            right = mid
        else:
            left = mid + 1

    return left


def repairCars(ranks: List[int], cars: int) -> int:
    r = max(ranks) * cars * cars
    l = 0

    def is_possible(mid):
        car_fixed = 0
        for rank in ranks:
            car_fixed += math.floor(math.sqrt(mid / rank))
        return car_fixed >= cars

    while l <= r:
        mid = (l + r) // 2
        if is_possible(mid):
            r = mid - 1
        else:
            l = mid + 1
    return l


def divideArray(nums: List[int]) -> bool:
    temp = Counter(nums)
    for _, v in temp.items():
        if v & 1:
            return False
    return True


# tag: bit manipulation, https://leetcode.com/problems/longest-nice-subarray
def longestNiceSubarray(nums: list[int]) -> int:
    used_bits = 0
    window_start = 0
    max_length = 0

    for index, num in enumerate(nums):
        while used_bits & num != 0:
            used_bits ^= nums[window_start]
            window_start += 1

        used_bits |= num
        max_length = max(max_length, index - window_start + 1)

    return max_length


def partitionArray(nums: List[int], k: int) -> int:
    nums.sort()
    ans = 0
    low = nums[0]
    for i in range(1, len(nums)):
        if abs(nums[i] - low) > k:
            ans += 1
            low = nums[i]
    return ans + 1


def genrateTag(caption: str) -> str:
    result = ["#"]
    words = caption.split()
    for ind, word in enumerate(words):
        if ind == 0:
            result.append(word[0].lower() + word[1:].lower())
        result.append(word[0].upper() + word[1:].lower())

    return "".join(result)


class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prime_cache = {}

        def is_prime_cached(num):
            if num not in prime_cache:
                prime_cache[num] = self.is_prime(num)
            return prime_cache[num]

        ans = 0

        for i in range(n):
            primes = []
            for j in range(i, n):
                if is_prime_cached(nums[j]):
                    primes.append(nums[j])

                if len(primes) >= 2:
                    min_prime = min(primes)
                    max_prime = max(primes)

                    if max_prime - min_prime <= k:
                        ans += 1
                    else:
                        break

        return ans

    def is_prime(self, n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True


def divideString(s: str, k: int, fill: str) -> List[str]:
    i, j = 0, k
    ans = []
    while i < len(s):
        temp = s[i:j]
        if len(temp) < k:
            temp = temp + fill * (k - len(temp))
        ans.append(temp)
        i = j
        j += k
    return ans


def kMirror(k: int, n: int):
    def is10mirror(i):
        if i.toString() == i.toString()[::-1]:
            return True
        return False

    def checkKmirror(i, k):
        num = 0
        base = 1
        while i > 0:
            digit = i % k
            num += digit * base
            base *= 10
            i //= k
        return str(num) == str(num)[::-1]

    count = 0
    ans = 0
    i = 1
    while count < n:
        if is10mirror(i) and checkKmirror(i, k):
            count += 1
            ans += i
        i += 1
    return ans


def max_subsequence(nums: List[int], k: int) -> List[int]:
    sorted_nums = sorted(enumerate(nums), key=lambda x: x[1])
    res = [x for i, x in sorted(sorted_nums[-k:])]
    return res


def num_subsequences(nums: List[int], target: int) -> int:
    nums.sort()
    ans = 0
    for ind, num in enumerate(nums):
        high = target - num
        high_index = bisect.bisect_right(nums, high) - 1
        if high_index < ind:
            continue
        ans += 2 ** (high_index - ind)
    return ans % (10**9 + 7)


def partitionString(s: str) -> List[str]:
    seen = set()
    ans = []
    i = 0
    temp = []
    while i < len(s):
        temp.append(s[i])
        if "".join(temp) not in seen:
            seen.add("".join(temp))
            ans.append("".join(temp))
            temp = []
        i += 1
    return ans


def find_LHS(nums: List[int]) -> int:
    nums.sort()
    has = {}
    for i, n in enumerate(nums):
        has[n] = i

    n = len(nums)
    max_len = 0
    for ind, num in enumerate(nums):
        if num + 1 in has:
            max_len = max(max_len, has[num + 1] - ind + 1)
    return max_len


def possibleStringCount(word: str) -> int:
    ans = 1
    prev = ""
    for ch in word:
        if ch != prev:
            prev = ch
        else:
            ans += 1
    return ans


def findWords(words: List[str]) -> List[str]:
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"
    ans = []

    def check(word):
        check = -1
        for ch in word:
            ch = ch.lower()
            if ch in first:
                temp = check
                check = 0
                if temp != -1 and temp != check:
                    return False
            if ch in second:
                temp = check
                check = 1
                if temp != -1 and temp != check:
                    return False
            if ch in third:
                temp = check
                check = 2
                if temp != -1 and temp != check:
                    return False
        return True

    for word in words:
        take = check(word)
        if take:
            ans.append(word)
    return ans


def finalString(s: str) -> str:
    temp = []
    for ind, ch in enumerate(s):
        if ch == "i":
            temp.append(ind)

    for ind, i in enumerate(temp):
        i = i - ind
        s = s[:i][::-1] + s[i + 1 :]
    return s


def kthCharacter(k: int, operations: List[int]) -> str:
    def find_upper_bound(k):
        upper_bound = 0
        temp = 1
        while temp < k:
            temp *= 2
            upper_bound += 1
        return upper_bound

    change = 0
    while k > 1:
        upper_bound = find_upper_bound(k)
        change += operations[upper_bound - 1]
        k = k - (2 ** (upper_bound - 1))
    return chr(change % 26 + 97)


def find_lucky(arr: List[int]) -> int:
    freq = Counter(arr)
    ans = -1
    for v, f in freq.items():
        if v == f and v > ans:
            ans = v

    return ans


# leetcode 1865, potd
class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.freq = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        temp = self.nums2[index]
        self.nums2[index] += val
        if temp + val not in self.freq:
            self.freq[temp + val] = 1
        else:
            self.freq[temp + val] += 1
        self.freq[temp] -= 1

    def count(self, tot: int) -> int:
        count = 0
        for i in self.nums1:
            if tot - i in self.freq:
                count += self.freq[tot - i]
        return count


def countKDifference(nums: List[int], k: int) -> int:
    nums.sort()
    freq = defaultdict(list)
    for ind, num in enumerate(nums):
        freq[num].append(ind)
    ans = 0
    for ind, num in enumerate(nums):
        if num + k in freq:
            indexes = freq[num + k]
            for i in indexes:
                if i > ind:
                    ans += 1
    return ans


# quite interesting problem, lc 2563, fair pairs
"""
Given a 0-indexed integer array nums of size n and two integers lower and upper, 
return the number of fair pairs.
A pair (i, j) is fair if:
    1. 0 <= i < j < n, and
    2. lower <= nums[i] + nums[j] <= upper

first condition doesn't matter as sum is associative. So we can do sorting.
Then use two pointers approach twice, first find all pair which are less than upper bound
and then find all pair which are less than lower bound and then we are done.
"""


def countFairPairs(nums: List[int], lower: int, upper: int) -> int:
    nums.sort()

    left, right = 0, len(nums) - 1
    count_within_upper = 0
    while left < right:
        if nums[left] + nums[right] <= upper:
            count_within_upper += right - left
            left += 1
        else:
            right -= 1

    left, right = 0, len(nums) - 1
    count_below_lower = 0
    while left < right:
        if nums[left] + nums[right] < lower:
            count_below_lower += right - left
            left += 1
        else:
            right -= 1
    return count_within_upper - count_below_lower


def maxEvents(events: List[List[int]]) -> int:
    events.sort()
    n = max(e[1] for e in events)
    min_heap = []
    ans = 0
    i = 0
    for day in range(1, n + 1):
        while i < len(events) and events[i][0] == day:
            heapq.heappush(min_heap, events[i][1])
            i += 1

        # remove the events that have ended
        while min_heap and min_heap[0] < day:
            heapq.heappop(min_heap)

        # attend event that starts today or earlier, one event a day
        if min_heap:
            heapq.heappop(min_heap)
            ans += 1

    return ans


def maxValue(self, events: List[List[int]], k: int) -> int:
    events.sort()
    starts = [e[0] for e in events]
    n = len(events)

    @lru_cache(maxsize=None)
    def dp(i: int, count: int) -> int:
        if i == n or count == k:
            return 0
        # Option 1: Skip this event
        skip = dp(i + 1, count)
        # Option 2: Take this event
        _, end, value = events[i]
        # Find the next event with start time > current end
        next_i = bisect.bisect_right(starts, end)
        take = value + dp(next_i, count + 1)
        return max(skip, take)

    return dp(0, 0)


def maxFreeTime(
    eventTime: int, k: int, startTime: List[int], endTime: List[int]
) -> int:

    gaps = [startTime[0]]
    n = len(startTime)
    for i in range(1, n):
        gaps.append(startTime[i] - endTime[i - 1])
    gaps.append(eventTime - endTime[-1])

    i = k + 1
    window_sum = sum(gaps[: k + 1])
    ans = window_sum
    while i <= len(gaps):
        window_sum += gaps[i] - gaps[i - (k + 1)]
        ans = max(ans, window_sum)
        i += 1

    return ans


def mostBooked(self, n: int, meetings) -> int:
    meetings.sort()
    room_meeting_count = [0] * n

    available_rooms = list(range(n))
    heapq.heapify(available_rooms)

    occupied_rooms = []

    for start, end in meetings:

        while occupied_rooms and occupied_rooms[0][0] <= start:
            end_time, room_number = heapq.heappop(occupied_rooms)
            heapq.heappush(available_rooms, room_number)

        duration = end - start

        if available_rooms:
            room_number = heapq.heappop(available_rooms)
            heapq.heappush(occupied_rooms, (end, room_number))
            room_meeting_count[room_number] += 1
        else:
            end_time, room_number = heapq.heappop(occupied_rooms)
            new_end = end_time + duration
            heapq.heappush(occupied_rooms, (new_end, room_number))
            room_meeting_count[room_number] += 1

    return room_meeting_count.index(max(room_meeting_count))


def earliestAndLatest(n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
    f = firstPlayer - 1
    s = secondPlayer - 1
    mn = float("inf")
    mx = float("-inf")

    @lru_cache(maxsize=None)
    def count(mask, i, j, round):
        nonlocal mn, mx
        if i >= j:
            count(mask, 0, n - 1, round + 1)
        elif mask & (1 << i) == 0:
            count(mask, i + 1, j, round)
        elif mask & (1 << j) == 0:
            count(mask, i, j - 1, round)
        elif i == f and j == s:
            mx = max(mx, round)  # type: ignore
            mn = min(mn, round)  # type: ignore
        else:
            if i != f and i != s:
                count(mask ^ (1 << i), i + 1, j - 1, round)
            if j != f and j != s:
                count(mask ^ (1 << j), i + 1, j - 1, round)

    count((1 << n) - 1, 0, n - 1, 1)
    return [mn, mx]  # type: ignore


def matchPlayersAndTrainers(players: List[int], trainers: List[int]) -> int:
    players.sort()
    trainers.sort()

    count = 0
    i, j = 0, 0
    while i < len(players) and j < len(trainers):
        if players[i] <= trainers[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1

    return count


def isLongPressedName(name: str, typed: str) -> bool:
    prev = typed[0]
    i = 1
    temp = (typed[0], 1)
    groups = []
    while i < len(typed):
        if typed[i] == prev:
            temp = (typed[i], temp[1] + 1)
            i += 1
            if i == len(typed):
                groups.append(temp)
        else:
            groups.append(temp)
            temp = (typed[i], 1)
            prev = typed[i]
            i += 1
    groups.append(temp)

    group2 = []
    j = 1
    prev = name[0]
    temp2 = (name[0], 1)
    while j < len(name):
        if name[j] == prev:
            temp2 = (name[j], temp2[1] + 1)
            j += 1
            if j == len(name):
                group2.append(temp2)
        else:
            group2.append(temp2)
            temp2 = (name[j], 1)
            prev = name[j]
            j += 1
    group2.append(temp2)

    if len(group2) != len(groups):
        return False

    else:
        for i in range(len(groups)):
            if group2[i][0] != groups[i][0] or group2[i][1] > groups[i][1]:
                return False

    return True


def maximizeGreatness(nums: List[int]) -> int:
    count = 0
    nums.sort()
    i, j = 0, 0
    while i < len(nums) and j < len(nums):
        if nums[i] < nums[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count


def maxProfitAssignment(
    difficulty: List[int], profit: List[int], worker: List[int]
) -> int:
    jobs = sorted(zip(difficulty, profit), key=lambda x: x[0])
    worker.sort()

    total_profit = 0
    max_profit = 0
    j = 0

    for w in worker:
        while j < len(jobs) and jobs[j][0] <= w:
            # since max difficulty doesn't guarantee max profit,
            # we need to keep track of max profit seen so far
            max_profit = max(max_profit, jobs[j][1])
            j += 1
        total_profit += max_profit

    return total_profit


# great use case of binary search
def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    pairs = []
    potions.sort()
    n = len(potions)
    for i in spells:
        if i * potions[-1] < success:
            pairs.append(0)
            continue
        low = 0
        high = n - 1
        while low <= high:
            mid = (low + high) // 2
            if potions[mid] * i >= success:
                high = mid - 1
            else:
                # it makes sure to point to least index for which potions[mid] * i >= success
                low = mid + 1
        pairs.append(n - low)
    return pairs


def isValid(word: str) -> bool:
    if len(word) < 3:
        return False

    word = word.lower()
    check_v = False
    check_c = False
    vowels = "aeiou"
    conson = "bcdfghjklmnpqrstvwxyz"

    for i in vowels:
        if i in word:
            check_v = True
    if check_v:
        for i in conson:
            if i in word:
                check_c = True
    else:
        return False
    if check_v and check_c and (word.isalnum() or word.isalpha()):
        return True
    return False


# the key idea to this problem was that there will be only 0,1 as remainder when dividing by 2
def maximumLength(nums: List[int]) -> int:
    if not nums:
        return 0
    even, odd = 0, 0

    for num in nums:
        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    evenOdd = 1
    prev = nums[0] % 2
    i = 1
    while i < len(nums):
        num = nums[i] % 2
        if prev != num:
            evenOdd += 1
            prev = num
        i += 1

    return max(even, odd, evenOdd)


def maximumGain(s: str, x: int, y: int) -> int:
    def get_max(first, second, s, maxi):
        stack = []
        ans = 0
        for ch in s:
            if ch == first and stack and stack[-1] == second:
                stack.pop()
                ans += maxi
            else:
                stack.append(ch)
        return "".join(stack), ans

    ans = 0
    if x > y:
        s, gain = get_max("a", "b", s, x)
        ans += gain
        _, gain = get_max("b", "a", s, y)
        ans += gain
    else:
        s, gain = get_max("b", "a", s, y)
        ans += gain
        _, gain = get_max("a", "b", s, x)
        ans += gain
    return ans


def maxSubarrays(n: int, conflictingPairs: List[List[int]]) -> int:
    valid = 0
    conflictingPoints = [[] for _ in range(n + 1)]

    for a, b in conflictingPairs:
        a, b = min(a, b), max(a, b)
        conflictingPoints[b].append(a)

    maxConflict = 0
    secondMaxConflict = 0
    extra = [0] * (n + 1)

    for end in range(1, n + 1):
        for u in conflictingPoints[end]:
            if u >= maxConflict:
                secondMaxConflict = maxConflict
                maxConflict = u
            elif u > secondMaxConflict:
                secondMaxConflict = u

        valid += end - maxConflict
        extra[maxConflict] += maxConflict - secondMaxConflict

    return valid + max(extra)


def countHillValley(nums: List[int]) -> int:
    temp = []
    prev = None
    for num in nums:
        if prev == num:
            continue
        prev = num
        temp.append(num)

    count = 0
    for i in range(1, len(temp) - 1):
        curr, prev, next = temp[i], temp[i - 1], temp[i + 1]
        if curr > prev and curr > next:
            count += 1
        if curr < prev and curr < next:
            count += 1
    return count


def smallestSubarrays(nums: List[int]) -> List[int]:
    max_or = 0
    for num in nums:
        max_or |= num

    l, r = 0, 0

    curr_or = 0
    ans = []
    while l <= r < len(nums):
        curr_or |= nums[r]
        if curr_or == max_or:
            ans.append(r - l + 1)
            l += 1
            r = l
            curr_or = 0
        else:
            r += 1
    return ans


def buildSegmentTree(index, left, right, baskets, segmentTree):
    if left == right:
        segmentTree[index] = baskets[left]
        return
    mid = (left + right) // 2
    buildSegmentTree(2 * index + 1, left, mid, baskets, segmentTree)
    buildSegmentTree(2 * index + 2, mid + 1, right, baskets, segmentTree)
    segmentTree[index] = max(segmentTree[2 * index + 1], segmentTree[2 * index + 2])


def querySegmentTree(index, left, right, fruit, segmentTree):
    if segmentTree[index] < fruit:
        return False

    if left == right:
        temp = segmentTree[index]
        segmentTree[index] = -1
        return temp >= fruit

    found = False
    mid = (left + right) // 2
    if segmentTree[2 * index + 1] >= fruit:
        found = querySegmentTree(2 * index + 1, left, mid, fruit, segmentTree)
    elif segmentTree[2 * index + 2] >= fruit:
        found = querySegmentTree(2 * index + 2, mid + 1, right, fruit, segmentTree)
    if found:
        segmentTree[index] = max(segmentTree[2 * index + 1], segmentTree[2 * index + 2])
    return found


def numOfUnplacedFruits(fruits: List[int], baskets: List[int]) -> int:
    n = len(baskets)
    segmentTree = [-1] * (4 * n)
    buildSegmentTree(0, 0, n - 1, baskets, segmentTree)
    unplaced = 0
    for fruit in fruits:
        if not querySegmentTree(0, 0, n - 1, fruit, segmentTree):
            unplaced += 1

    return unplaced


def longestSubarray(nums):
    maxi = float("-inf")
    maxi_without_zero = float("-inf")
    left, right = 0, 0
    n = len(nums)
    zeros = 0
    while left <= right < n:
        if nums[right] == 0:
            zeros += 1
        if zeros <= 1:
            if zeros == 0:
                maxi_without_zero = max(maxi_without_zero, right - left + 1)
            maxi = max(maxi, right - left + 1)
            right += 1
        else:
            if nums[left] == 0:
                zeros -= 1
            left += 1
    if maxi_without_zero > maxi:
        return maxi_without_zero - 1
    return maxi - 1


def sumZero(n: int) -> List[int]:
    ans = []
    is_odd = n & 1 == 0
    temp = n // 2
    for i in range(1, temp + 1):
        if is_odd and i == n // 2:
            ans.append(0)
        ans.append(i)
        ans.append(-i)
        temp -= 1
    return ans


def countOperations(num1: int, num2: int) -> int:
    ans = 0
    while num1 != 0 and num2 != 0:
        ans += 1
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
    return ans


# leetcode 3738, biweekly contest 8/11/2025
def longestNonDecreasing(nums):
    n = len(nums)
    if n == 1:
        return 1

    left = [1] * n
    right = [1] * n

    for i in range(1, n):
        if nums[i] >= nums[i - 1]:
            left[i] = left[i - 1] + 1

    for i in range(n - 2, -1, -1):
        if nums[i] <= nums[i + 1]:
            right[i] = right[i + 1] + 1

    ans = max(left)
    if ans != n:
        ans += 1
    for i in range(1, n - 1):
        if nums[i - 1] <= nums[i + 1]:
            ans = max(ans, left[i - 1] + right[i + 1] + 1)
    return ans


def countTrapezoids(points: List[List[int]]) -> int:
    dy = defaultdict(set)
    for point in points:
        dy[point[1]].add(point[0])

    temp = []
    for x, y in dy.items():
        temp.append(len(y))

    ans = 0
    for ind, i in enumerate(temp):
        for j in range(ind + 1, len(temp)):
            ans += i * (temp[j] - 1)
    return ans


# print(countTrapezoids([[1, 0], [2, 0], [3, 0], [2, 2], [3, 2]]))


def sumFourDivisors(nums: List[int]) -> int:
    ans = 0
    for ele in nums:
        temp = [1, ele]
        for i in range(2, int(math.sqrt(ele)) + 1):
            if ele % i == 0:
                temp.append(i)
                if ele // i != i:
                    temp.append(ele // i)
            if len(temp) > 4:
                break
        if len(temp) == 4:
            ans += sum(temp)
    return ans


# need to watch solution video for this
# https://leetcode.com/problems/count-subarrays-with-majority-element-ii/description/
