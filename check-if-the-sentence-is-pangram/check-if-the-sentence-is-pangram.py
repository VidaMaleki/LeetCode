class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        s_set = set(sentence)
        if len(s_set) == 26:
            return True
        return False