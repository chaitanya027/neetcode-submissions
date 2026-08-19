class Solution:
    def isValid(self, st: str) -> bool:
        validSet = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack = []

        for s in st:
            if s in validSet.keys():
                if not stack or stack.pop() != validSet[s]:
                    return False
            if s in validSet.values():
                stack.append(s)
        
        return not stack