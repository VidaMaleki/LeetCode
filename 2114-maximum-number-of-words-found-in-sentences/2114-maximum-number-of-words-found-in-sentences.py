class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        total = []
        count_space = 0
        for sentence in sentences:
            count_space = sentence.count(" ") + 1
            total.append(count_space)
        return max(total)