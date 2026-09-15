class Solution:
    def isValid(self, s: str) -> bool:
        d=[]
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for i in s:
            print(d,i in pairs)
            if i in pairs:
                
                if not d or d.pop() != pairs[i]:
                    return False
            else:
                d.append(i)
        return not d

        