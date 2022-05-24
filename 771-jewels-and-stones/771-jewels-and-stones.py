class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        matched = []
        for stone in stones:
            if stone in jewels:
                matched.append(stone)
            
        return len(matched)