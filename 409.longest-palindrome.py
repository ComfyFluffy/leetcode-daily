#
# @lc app=leetcode id=409 lang=python3
#
# [409] Longest Palindrome
#


# @lc code=start
class Solution:

    def longestPalindrome(self, s: str) -> int:
        d: dict[str, int] = {}
        for x in s:
            d[x] = (d.get(x) or 0) + 1
        d = {
            k: v
            for k, v in sorted(
                d.items(), key=lambda item: item[1], reverse=True)
        }
        l = 0
        with_odd = False
        for _, v in d.items():
            if v % 2 == 0:
                l += v
            elif not with_odd:
                l += v
                with_odd = True
            else:
                l += v // 2 * 2
        return l


# @lc code=end
Solution().longestPalindrome(
    'civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth'
)
