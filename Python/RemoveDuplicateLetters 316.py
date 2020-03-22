class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = {}
        for c in s:
            counter[c] = counter.get(c, 0)+1
        res = []
        visited = set()
        for c in s:
            counter[c] -= 1
            # when a new letter come, try to use it to replace as many letters in res before it as possible
            if c not in visited:
                while res and c < res[-1] and counter[res[-1]] >= 1:
                    visited.remove(res[-1])
                    res.pop()
                res.append(c)
                visited.add(c)
        return ''.join(res)
