class Solution(object):
    def maxArea(self, height):
        a = 0
        for i in range(len(height)):
            h1 = height[i]
            for j in range(i+1, len(height)):
                w = j - i
                h2 = height[j]
                h = min(h1, h2)
                a = max(h * w, a)
        return a


        