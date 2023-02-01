class Solution:
    def removeVowels(self, s: str) -> str:
        vowels = 'aeiou'
        answer = ""
        for i in s:
            if i not in vowels:
                answer += i
        return answer
                
        