class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1, dic2 = {}, {}
        
        for i in s1: 
            dic1[i] = dic1.get(i, 0) + 1
        
        m, n = len(s1), len(s2)
        
        if m > n:
            return False
        
        for i in range(m):
            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
        
        for i in range(m, n):
            if dic1 == dic2:
                return True

            dic2[s2[i]] = dic2.get(s2[i], 0) + 1
            
            dic2[s2[i - m]] -= 1
            if dic2[s2[i - m]] == 0:
                del dic2[s2[i - m]]
        
        return dic1 == dic2
        


#567. Permutation in String


Given two strings s1 and s2, return true if s2 contains a 
permutation
 of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.

