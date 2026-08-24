class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return "@#"
        s = "*$".join(strs)
        return s
    def decode(self, s: str) -> List[str]:
        if s=="@#":
            return []
        return s.split("*$")