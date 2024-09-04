def trap(self, height: List[int]) -> int:
    rain, max_l, max_r = 0, height[l := 0], height[r := len(height) - 1]

    while l <= r:
        if max_l < max_r:
            max_l = max(max_l, height[l])
            rain += max_l - height[l]
            l += 1
        else:
            max_r = max(max_r, height[r])
            rain += max_r - height[r]
            r -= 1

    return rain
