# Write a function that reverses a string. The input string is given as an array of characters s.

# You must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]


def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s)

    while left < right:
        print("left: ", left, "right: ", right)
        temp = s.pop()
        s.insert(left, temp)
        left +=1

    return s