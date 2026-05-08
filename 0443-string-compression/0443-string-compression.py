class Solution:
    def compress(self, chars: List[str]) -> int:
        #chars = ["a","a","b","b","c","c","c"]
        #           a, 
        i = 0
        start = 0
        write = 0
        while i < len(chars):
            count = 0
            while i < len(chars) and chars[i] == chars[start]:
                i += 1
                count = i - start

            chars[write] = chars[start]
            write += 1
            if count > 1:
                for num in str(count):
                    chars[write] = num
                    write += 1

            start = i
            
        return write

        
        


        
