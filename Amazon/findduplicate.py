from typing import List


def findDuplicate(nums: List[int]) -> int:
    nums_dict = dict()
    for num in nums:
        if num not in nums_dict:
            nums_dict[num] = True
        else:
            return num


TEST_ARRAY = [1, 3, 4, 2, 2]
TEST_ARRAY2 = [3, 1, 3, 4, 2]

print(findDuplicate(TEST_ARRAY))
print(findDuplicate(TEST_ARRAY2))
