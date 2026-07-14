class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:

        ans = 0

        for sentence in sentences:

            words = len(sentence.split())

            ans = max(ans, words)

        return ans
        