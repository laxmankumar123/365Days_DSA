class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        string ans="";
        while(true){
            if(a!=0 and a>=b and a>=c){
                if(ans=="" || ans[ans.size()-1]!='a'){
                    if(a==1 || a<=b+c){
                        ans+='a';
                        a-=1;
                    }
                    else{
                        ans+="aa";
                        a-=2;
                    }
                }
                else{
                    if(b==0 and c==0){
                        break;
                    }
                    if(b>=c){
                        if(b==1 || b<=a+c){
                            ans+='b';
                            b-=1;
                        }
                        else{
                            ans+="bb";
                            b-=2;
                        }
                    }
                    else{
                        if(c==1 || c<=b+a){
                            ans+='c';
                            c-=1;
                        }
                        else{
                            ans+="cc";
                            c-=2;
                        }
                    }
                }
                
            }
            // else if(b!=0 and a<=b and b>=c){
            //     if(ans=="" || ans[ans.size()-1]!='b'){
            //         if(b==1 || b<=a+c){
            //             ans+='b';
            //             b-=1;
            //         }
            //         else{
            //             ans+="bb";
            //             b-=2;
            //         }
            //     }
            //     else{
            //         if(a==0 and c==0){
            //             break;
            //         }
            //         if(a>=c){
            //             if(a==1 || a<=b+c){
            //                 ans+='a';
            //                 a-=1;
            //             }
            //             else{
            //                 ans+="aa";
            //                 a-=2;
            //             }
            //         }
            //         else{
            //             if(c==1 || c<=b+a){
            //                 ans+='c';
            //                 c-=1;
            //             }
            //             else{
            //                 ans+="cc";
            //                 c-=2;
            //             }
            //         }
            //     }
                
            // }
            // else if(c!=0 and a<=c and b<=c){
            //     if(ans=="" || ans[ans.size()-1]!='c'){
            //         if(c==1 || c<=b+a){
            //             ans+='c';
            //             c-=1;
            //         }
            //         else{
            //             ans+="cc";
            //             c-=2;
            //         }
            //     }
            //     else{
            //         if(b==0 and a==0){
            //             break;
            //         }
            //         if(a>=b){
            //             if(a==1 || a<=b+c){
            //                 ans+='a';
            //                 a-=1;
            //             }
            //             else{
            //                 ans+="aa";
            //                 a-=2;
            //             }
            //         }
            //         else{
            //             if(b==1 || b<=a+c){
            //                 ans+='b';
            //                 b-=1;
            //             }
            //             else{
            //                 ans+="bb";
            //                 b-=2;
            //             }
            //         }
            //     }
                
            // }
            else{
                break;
            }
        }
        return ans;
    }
};




#1405. Longest Happy String


A string s is called happy if it satisfies the following conditions:

s only contains the letters 'a', 'b', and 'c'.
s does not contain any of "aaa", "bbb", or "ccc" as a substring.
s contains at most a occurrences of the letter 'a'.
s contains at most b occurrences of the letter 'b'.
s contains at most c occurrences of the letter 'c'.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: a = 1, b = 1, c = 7
Output: "ccaccbcc"
Explanation: "ccbccacc" would also be a correct answer.
Example 2:

Input: a = 7, b = 1, c = 0
Output: "aabaa"
Explanation: It is the only correct answer in this case.
 

Constraints:

0 <= a, b, c <= 100
a + b + c > 0