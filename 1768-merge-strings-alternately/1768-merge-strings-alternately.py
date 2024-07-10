class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = ""
        i = 0
        j = 0
        while i < len(word1) and j < len(word2):
            print(word1[i] , word2[j])
            answer += word1[i] + word2[j]
            i += 1
            j += 1
            
        if i != len(word1):
            answer += word1[i:]
        if j != len(word2) :
            answer += word2[j:]
        return answer