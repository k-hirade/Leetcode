class Solution(object):
    def isValid(self, s):
        chara = {")": "(", "}": "{", "]": "[", }
        stack = []
        for char in s:
            if char in chara:
                top_element = stack.pop() if stack else '#'
                if chara[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack
