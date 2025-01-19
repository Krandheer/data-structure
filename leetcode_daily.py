import heapq
from collections import Counter, defaultdict
import math
from typing import List
from collections import deque


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


print(trapRainWater([[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]))
