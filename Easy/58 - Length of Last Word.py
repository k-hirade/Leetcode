class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split(" ")
        return len(words[-1])
# strip() : 文字列の両端にある特定の文字を削除
# split() : 文字列ないの特定の文字で文字列を区切り、それを配列にして返す
