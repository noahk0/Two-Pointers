def twoSum(self, numbers: List[int], target: int) -> List[int]:
    left, right = 0, len(numbers) - 1

    while left < right:
        candidate = numbers[left] + numbers[right]

        if candidate < target:
            left += 1
        elif target < candidate:
            right -= 1
        else:
            return (left + 1, right + 1)
