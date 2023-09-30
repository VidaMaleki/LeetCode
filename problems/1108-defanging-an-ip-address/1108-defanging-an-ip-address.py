class Solution:
    def defangIPaddr(self, address: str) -> str:
        defang = []
        for i in address:
            if i == ".":
                defang.append("[.]")
            else:
                defang.append(i)
        return "".join(defang)