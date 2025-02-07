import heapq
from collections import Counter, defaultdict, deque
import math
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


print(queryResults(4, [[1, 4], [2, 5], [1, 3], [3, 4]]))
