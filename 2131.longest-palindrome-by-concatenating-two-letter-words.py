#
# @lc app=leetcode id=2131 lang=python3
#
# [2131] Longest Palindrome by Concatenating Two Letter Words
#

# @lc code=start
from collections import Counter


class Solution:

    def longestPalindrome1(self, words: list[str]) -> int:
        result = 0

        unpaired = set()

        for w in words:
            rw = w[::-1]
            if rw in unpaired:
                unpaired.remove(rw)
                result += 2
            else:
                unpaired.add(w)

        for w in unpaired:
            if w[0] == w[1]:
                result += 1
                break
        print(unpaired)
        return result * 2

    def longestPalindrome(self, words: list[str]) -> int:
        # a count variable contains the number of occurrences of each word
        count = Counter(words)
        answer = 0
        central = False
        for word, count_of_the_word in count.items():
            # if the word is a palindrome
            if word[0] == word[1]:
                if count_of_the_word % 2 == 0:
                    answer += count_of_the_word
                else:
                    answer += count_of_the_word - 1
                    central = True
            # consider a pair of non-palindrome words,
            # such that one is the reverse of another
            # word[1] + word[0] is the reversed word
            elif word[0] < word[1]:
                answer += 2 * min(count_of_the_word, count[word[1] + word[0]])
        if central:
            answer += 1
        return 2 * answer


# @lc code=end
# print(Solution().longestPalindrome(["lc", "cl", "gg"]))
# print(Solution().longestPalindrome(["ab", "ty", "yt", "lc", "cl", "ab"]))
# print(Solution().longestPalindrome(["cc", "ll", "xx"]))
print(Solution().longestPalindrome([
    "qo", "fo", "fq", "qf", "fo", "ff", "qq", "qf", "of", "of", "oo", "of",
    "of", "qf", "qf", "of"
]))
