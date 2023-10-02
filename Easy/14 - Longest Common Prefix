class Solution(object):
    def longestCommonPrefix(self, strs):
        for i, chars in enumerate(zip(*strs)):
            if len(set(chars)) > 1:
                return strs[0][:i]

        return min(strs, key=len)
        # strs = ["abc", "abd", "ace"] -> ('a', 'a', 'a'), ('b', 'b', 'c'), ('c', 'd', 'e')
        # set() -> check the number of duplicate
