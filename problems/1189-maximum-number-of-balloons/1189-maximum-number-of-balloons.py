class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_dict = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        text_dict = {}
        for char in text:
            text_dict[char] = text_dict.get(char, 0) +1
            
        print(text_dict)
        if not "b" in text_dict:
            return 0
        if not "a" in text_dict:
            return 0
        if not "l" in text_dict:
            return 0
        if not "o" in text_dict:
            return 0
        if not "n" in text_dict:
            return 0
        text_dict["l"] = text_dict["l"] // 2
        text_dict["o"] = text_dict["o"] // 2
        
        return min(text_dict["b"],text_dict["a"], text_dict["l"], text_dict["o"], text_dict["n"])