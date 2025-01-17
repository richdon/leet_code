def search(nums: list[int], target: int) -> int:
    left_ptr, right_ptr = 0, len(nums) - 1
    mid = (left_ptr + right_ptr) // 2
    while left_ptr <= right_ptr:
        if nums[mid] == target:
            return mid
        if target > nums[mid]:
            # narrow to the right
            left_ptr = mid + 1
        else:
            # narrow to the right
            right_ptr = mid - 1
        mid = (left_ptr + right_ptr) // 2
    return -1


print(search([5], 5))
