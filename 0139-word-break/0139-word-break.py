class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            if not dp[i]:
                continue
            for j in range(i + 1, len(s) + 1):
                if s[i:j] in word_set:
                    dp[j] = True
        return dp[len(s)]