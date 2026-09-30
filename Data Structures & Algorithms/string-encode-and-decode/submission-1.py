class Solution:
    MARKER = "MARKER"
    def encode(self, strs: List[str]) -> str:
        result = ""
        for string in strs:
            result += string
            result += self.MARKER
        return result
    def decode(self, s: str) -> List[str]:
        result = s.split(self.MARKER)
        return result[:-1]