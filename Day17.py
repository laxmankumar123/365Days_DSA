class Solution:
    def maximumSwap(self, num: int) -> int:
        str1=str(num)
        arr1=[]
        result=0
        for i in str1:
            arr1.append(i)
        for j in range(0,len(str1)):
            for i in range(0,len(str1)):
                arr2=[]
                arr2.extend(arr1)
                var=arr2[j]
                arr2[j]=arr2[i]
                arr2[i]=var
                str2=""
                for letter in arr2:
                    str2+=str(letter)
                result=max(result,int(str2))
        return result
        
# 670. Maximum Swap



You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108