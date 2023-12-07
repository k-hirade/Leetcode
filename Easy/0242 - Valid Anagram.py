class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      if s is None or t is None or len(s) != len(t):
        return False

      return True if sorted(s) == sorted(t) else False
