class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        if len(nums)==1:
            return 1
        dict1 = {}
        for num in nums:
            if (num in dict1):
                dict1[num] += 1
            else:
                dict1[num] = 1

        m=max(dict1.values())

        max_element=[k for k in dict1 if dict1.get(k) == m]
        c=[]
        for d in max_element:
            visited=0
            first_post=0
            last_post=0
            for i in range(0,len(nums)):
                if d == nums[i] and visited==0:
                    first_post=i
                    visited+=1
                    
                if d== nums[i] and visited>=1:
                    last_post=i
                    visited+=1
                else:
                    pass
            pos=last_post-first_post
            pos=pos+1
            c.append(pos)
        
        return min(c)


#697. Degree of an Array


Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.

 

Example 1:

Input: nums = [1,2,2,3,1]
Output: 2
Explanation: 
The input array has a degree of 2 because both elements 1 and 2 appear twice.
Of the subarrays that have the same degree:
[1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
The shortest length is 2. So return 2.
Example 2:

Input: nums = [1,2,2,3,1,4,2]
Output: 6
Explanation: 
The degree is 3 because the element 2 is repeated 3 times.
So [2,2,3,1,4,2] is the shortest subarray, therefore returning 6.
 

Constraints:

nums.length will be between 1 and 50,000.
nums[i] will be an integer between 0 and 49,999.




