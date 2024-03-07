# Okay, let's make this really simple, like we're explaining it to a 5-year-old:

# Imagine you have a box of colored blocks. Some blocks have the same color, and you like all the colors,
# but you want to make sure you have room for as many different colors as possible.
# However, you really like some colors, so you decide it's okay to have two blocks of the same color,
# but not more than two.

# So, you start looking at your blocks one by one. The first two blocks are special; you decide you can
# keep them no matter what. Then, you start looking at the rest of the blocks.
# Each time you pick up a block, you check:

# - If it's a new color you don't have in your special box yet, or it's a second block of the same color
# you like, you put it in the special box to keep.
# - But, if it's the third (or more) block of the same color, you decide not to put it in your special box
# because you want to save space for other colors.

# In the end, you count how many blocks you have in your special box, and that's your answer!

# In the computer code, we did something similar with numbers instead of blocks.
# We looked through a list of numbers, and if we found a number that was either new or
# only repeated once before, we kept it in the "special box" (which is the first part of the list).
# If it was repeated more than twice, we didn't keep it. In the end,
# we told you how many numbers we kept in the special box, which was 5 in our example.
# And the numbers we kept were like your favorite blocks: 1, 1, 2, 2, 3.


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:  # If the list is really short, we don't need to do anything!
            return len(nums)  # Just say how many things are in the list.

        j = 2  # We start checking from the third spot because the first two are always okay.

        for i in range(
            2, len(nums)
        ):  # Now, we start looking from the third thing to the end.
            if (
                nums[i] != nums[j - 2]
            ):  # If the thing we're looking at is different from the one two spots back...
                nums[j] = nums[i]  # We can keep it and move it to the new spot.
                j += 1  # And we get ready for the next new spot.

        return j  # We tell how many unique things we have at the end.


# Create an instance of the Solution class
solution = Solution()

# Example array
nums = [1, 1, 1, 2, 2, 3]

# Call the method and store the result
k = solution.removeDuplicates(nums)

# Print the modified array and the value of k
print("Modified array:", nums[:k])
print("k:", k)
