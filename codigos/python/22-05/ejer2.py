class Solution:
    def partitionRec(self, l ,s: str) -> List[List[str]]:
        if len(s) == 0:
            return l
        for i in range(len(s)):
            if isPalindrome(s[:i+1]):
                l.append(s[:i+1])
                return partitionRec(l, s[i+1:])
        return l


    def isPalindrome(self, s:str) -> bool:
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        ret = []

        for i in range(len(s)):
            ret += partitionRec(ret, s[i:])

        return ret