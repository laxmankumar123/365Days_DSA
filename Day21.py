class Solution {
public:
    void find(string &s, int i, int n, set<string> &st, int &res){
        if(i==n){
            res=max(res,(int)st.size());
            return;
        }
        string temp="";
        for(int j=i;j<n;j++){
            temp+=s[j];
            cout<<temp<<endl;
            if(st.count(temp)==0){
                st.insert(temp);
                find(s, j+1, n, st, res);
                st.erase(temp);
            }
        }
        return;
    }
    int maxUniqueSplit(string s) {
        // backtracking
        // recursion
        // set
        // string
        // pratition
        set<string> st;
        int res=0;
        find(s,0 , s.size(), st, res);
        return res;
    }
};




#593. Split a String Into the Max Number of Unique Substrings

Given a string s, return the maximum number of unique substrings that the given string can be split into.

You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "ababccc"
Output: 5
Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
Example 2:

Input: s = "aba"
Output: 2
Explanation: One way to split maximally is ['a', 'ba'].
Example 3:

Input: s = "aa"
Output: 1
Explanation: It is impossible to split the string any further.
 

Constraints:

1 <= s.length <= 16

s contains only lower case English letters.
