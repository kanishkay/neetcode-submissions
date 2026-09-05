class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Store the pairs in a hash map
        map = {}

        for i,num in enumerate(nums):
            # Calculate the required number to reach the target
            complement = target - num

            # If complement is already in the map
            if complement in map:
                return [map[complement], i]
            
            # If not found, store the current number and its index
            map[num] = i
        

        