def threeSum(self, nums: List[int]) -> List[List[int]]:
    nums.sort()
    triplet, end = [], len(nums) - 1

    for left in range(end):
        if nums[left] > 0:
            break

        if left and nums[left] == nums[left - 1]:
            continue

        right, center = end, left + 1

        while center < right:
            three = nums[left] + nums[center] + nums[right]

            if 0 < three:
                right -= 1
            elif three < 0:
                center += 1
            else:
                triplet.append((nums[left], nums[center], nums[right]))

                right -= 1
                center += 1

                while center < right and nums[center] == nums[center - 1]:
                    center += 1

    return triplet
