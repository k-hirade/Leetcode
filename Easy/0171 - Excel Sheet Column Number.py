class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for char in columnTitle:
            # ord() -> 1文字のユニコード文字を表す文字列に対し、その文字のユニコードポイントを表す整数を返す。charの逆
            result = result*26 + (ord(char) - ord('A') + 1)
        return result
