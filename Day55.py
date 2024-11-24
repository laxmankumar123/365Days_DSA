class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def calculate_max_amount(index):
            if index>=len(nums):
                return 0
            if index in memo:
                return memo[index]
            skip_current_house = calculate_max_amount(index + 1)

            rob_current_house = nums[index] + calculate_max_amount(index + 2)
            
            memo[index] = max(skip_current_house, rob_current_house)
            return memo[index]
        return calculate_max_amount(0)
