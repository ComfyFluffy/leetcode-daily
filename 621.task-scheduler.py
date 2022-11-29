#
# @lc app=leetcode id=621 lang=python3
#
# [621] Task Scheduler
#

# @lc code=start
from collections import Counter


class Solution:

    # def leastInterval(self, tasks: list[str], n: int) -> int:
    #     if n == 0:
    #         return len(tasks)

    #     count = {
    #         k: v
    #         for k, v in sorted(
    #             Counter(tasks).items(), key=lambda item: item[1], reverse=True)
    #     }
    #     result = 0
    #     last_idles = 0
    #     while len(count):
    #         to_pop = []
    #         current = 0
    #         if min(count.values()) >= 2:
    #             g = count.items()
    #         else:
    #             g = (x for _, x in zip(range(n + 1), count.items()))
    #         for k, v in g:
    #             if v == 1:
    #                 to_pop.append(k)
    #             else:
    #                 count[k] -= 1
    #             current += 1

    #         result += current
    #         last_idles = current - len(count)

    #         for k in to_pop:
    #             count.pop(k)
    #     result -= last_idles
    #     return result

    def leastInterval(self, tasks: list[str], n: int) -> int:
        task_counts = list(Counter(tasks).values())
        max_count = max(task_counts)
        count_of_max_count = task_counts.count(max_count)
        return max(len(tasks), (max_count - 1) * (n + 1) + count_of_max_count)


# @lc code=end
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2))
print(Solution().leastInterval(
    ["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2))
print(Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 0))
print(Solution().leastInterval(
    ["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2))
