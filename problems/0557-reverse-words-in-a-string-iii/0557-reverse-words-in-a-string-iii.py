class Solution:
    def reverse(self, s):
        return s[::-1]
    
    def reverseWords(self, s: str) -> str:
        new_list = []
        splited_s= s.split(" ")
        print(splited_s)
        for word in splited_s:
            temp = self.reverse(word)
            new_list.append(temp)
        print(new_list)
        return " ".join(new_list)