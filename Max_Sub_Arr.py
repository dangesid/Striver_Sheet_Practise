# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

max_so_far = float('-inf')
max_ending_here = 0
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
for i in range(0, n):
    max_ending_here = max_ending_here + arr[i]
    if max_so_far < max_ending_here:
        max_so_far = max_ending_here
    if max_ending_here < 0:
        max_ending_here = 0
print(max_so_far)
