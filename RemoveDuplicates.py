# Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.


class Solution:
    def removeDuplicates(self, nums):
        # If our line of beads is empty or has just one bead,
        # we don't need to do anything!
        if not nums:
            return 0

        # We start with our first bead in hand.
        unique_bead = 0

        # Now, we look at each bead, one by one, starting with the second.
        for i in range(1, len(nums)):
            # If the bead I'm looking at is not the same as the one in my hand,
            if nums[i] != nums[unique_bead]:
                # I move to the next spot to place a new unique bead.
                unique_bead += 1
                # And I put this new, different bead in the next spot.
                nums[unique_bead] = nums[i]

        # At the end, I count all the unique beads I have placed in a row.
        # I add 1 because I started counting from 0.
        return unique_bead + 1


# Let's sort our beads!
solution = Solution()

# We have a line of beads, some are the same color.
beads1 = [1, 1, 2]  # Imagine these are colors.
print("Sorting beads 1:")
# We sort them with our method.
unique_beads1 = solution.removeDuplicates(beads1)
# We show how many unique colors we have, and what our new line looks like.
print(f"We have {unique_beads1} unique beads, they are {beads1[:unique_beads1]}!")

beads2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]  # Another line of beads with more colors.
print("\nSorting beads 2:")
unique_beads2 = solution.removeDuplicates(beads2)
print(f"We have {unique_beads2} unique beads, they are {beads2[:unique_beads2]}!")
