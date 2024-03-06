# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place.
# The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

# Consider the number of elements in nums which are
# not equal to val be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the elements which are not equal to val.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int val = ...; // Value to remove
# int[] expectedNums = [...]; // The expected answer with correct length.
#                             // It is sorted with no values equaling val.

# int k = removeElement(nums, val); // Calls your implementation

# assert k == expectedNums.length;
# sort(nums, 0, k); // Sort the first k elements of nums
# for (int i = 0; i < actualLength; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.



class Solution:
    def removeElement(self, nums, val):
        favorite = 0  # Start at the beginning of the galaxy
        for planet in nums:
            if planet != val:  # If the planet is not a space rock
                nums[favorite] = planet  # Keep it in the safe zone
                favorite += 1  # Count it as a valuable planet
        return favorite  # Return how many valuable planets we have


# Create an instance of the spaceship
spaceship = Solution()

# Our galaxy with planets and space rocks
galaxy1 = [3, 2, 2, 3]
space_rock = 3
print("In our first galaxy mission:")
k1 = spaceship.removeElement(galaxy1, space_rock)
print(f"We secured {k1} planets, and they are {galaxy1[:k1]}!")

galaxy2 = [0, 1, 2, 2, 3, 0, 4, 2]
print("\nIn our second galaxy mission:")
k2 = spaceship.removeElement(galaxy2, space_rock)
print(f"We secured {k2} planets, and they are {galaxy2[:k2]}!")
