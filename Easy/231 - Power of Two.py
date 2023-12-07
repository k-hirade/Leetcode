class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
            # ビット単位のAND演算
            # 両方のビットが1である場合のみ、結果のそのビットを1に設定する
        return n & (n - 1) == 0
