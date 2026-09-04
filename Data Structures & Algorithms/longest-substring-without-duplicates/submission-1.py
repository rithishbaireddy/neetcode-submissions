class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        charset=set()
        
        result=0
        for right in range(len(s)):
            while s[right] in charset:
                charset.remove(s[left])
                left+=1
            charset.add(s[right])

            result=max(result,right-left+1)
        return result    



        

        