def maxArea(self, height: List[int]) -> int:
    vol, l, r = 0, 0, len(height) - 1

    while l < r:
        if height[l] < height[r]:
            vol = max(vol, height[l] * (r - l))
            l += 1
        else:
            vol = max(vol, height[r] * (r - l))
            r -= 1

    return vol
