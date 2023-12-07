# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        def findTarget(mountain_arr):
            left , right = 0 , mountain_arr.length() -1
            while right > left:

                mid = (right + left )//2

                if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        def binary_search(mountain_arr, left, right, target, is_asc):
            while left <= right:
                mid = left + (right - left) // 2
                mid_val = mountain_arr.get(mid)
                if mid_val == target:
                    return mid
                if (is_asc and mid_val < target) or (not is_asc and mid_val > target):
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        p = findTarget(mountain_arr)

        result = binary_search(mountain_arr, 0, p, target, True)
        if result != -1:
            return result

        return binary_search(mountain_arr, p+ 1, mountain_arr.length() - 1, target, False)

    
    
    