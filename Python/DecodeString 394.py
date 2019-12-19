class Solution:
    def decodeString(self, s: str) -> str:
        n = len(s)
        stack = []
        for i in range(n):
            if s[i] == ']':
                chars = []
                while stack and stack[-1] != '[':
                    chars.append(stack.pop())
                chars = ''.join(chars[::-1])
                stack.pop()
                nums, digit = 0, 1
                while stack and stack[-1].isdigit():
                    nums += int(stack.pop()) * digit
                    digit *= 10
                stack.append( max(nums, 1) * chars )
            else:
                stack.append(s[i])
        return ''.join(stack)
