class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check if the current plot is the first plot
                if i == 0:
                    if len(flowerbed) == 1 or flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                # Check if the current plot is the last plot
                elif i == len(flowerbed) - 1:
                    if flowerbed[i-1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                # Check if the current plot is in the middle
                else:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
            if n <= 0:
                return True
        return False

        