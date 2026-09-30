class Solution:
    MARKER = "MARKER"
    def encode(self, strs: List[str]) -> str:
        result = []
        for string in strs:
            result.append(string)
            result.append(self.MARKER)
        return "".join(result)
    def decode(self, s: str) -> List[str]:
        result = s.split(self.MARKER)
        return result[:-1]