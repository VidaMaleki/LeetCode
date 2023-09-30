class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        right = len(s)-1
        reversed_vowels = []
        while right >= 0:
            if s[right].lower() in vowels:
                reversed_vowels.append(s[right])
            right -= 1
        print("reversed_vowels", reversed_vowels)
        j =0
        answer =""
        for i in s:
            if i.lower() in vowels:
                answer += reversed_vowels[j]
                j +=1
            else:
                answer += i
        return answer