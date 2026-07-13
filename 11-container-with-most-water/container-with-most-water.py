class Solution:
    def maxArea(self, height: List[int]):

        i = 0
        j = len(height) - 1

        ans = 0

        while i < j:

            width = j - i

            h = min(height[i], height[j])

            water = width * h

            ans = max(ans, water)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return ans