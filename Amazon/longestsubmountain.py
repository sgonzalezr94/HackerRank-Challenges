from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        mountain = []
        for i in range(len(arr)):
            if not mountain:
                mountain.append(arr[i])
            else:
                if arr[i + 1] > mountain[i]:
                    mountain.append(arr[i])
                else:
                    pass
