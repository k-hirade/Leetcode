class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_to_t, t_to_s = {}, {}
        # 二つの文字列の各文字に対してループ
        # 同じ長さの文字列でないといけない
        for char_s, char_t in zip(s, t):
            if (char_s in s_to_t and s_to_t[char_s] != char_t) or (char_t in t_to_s and t_to_s[char_t] != char_s):
                return False
            s_to_t[char_s] = char_t
            t_to_s[char_t] = char_s

        return True
