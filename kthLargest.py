class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = []
        for n in nums:
            self.add(n)

    def get_parent_idx(self, i):
        return i // 2

    def should_swap(self, idx):
        if idx == 0:
            return False
        parent_idx = self.get_parent_idx(idx)
        return self.nums[idx] < self.nums[parent_idx]

    def swap(self, idx, element):
        parent_idx = self.get_parent_idx(idx)
        self.nums[idx] = self.nums[parent_idx]
        self.nums[parent_idx] = element
        return parent_idx

    def heapify_up(self):
        idx = len(self.nums) - 1
        should_swap = self.should_swap(idx)
        while should_swap:
            element = self.nums[idx]
            if idx == self.k:
                return element
            idx = self.swap(idx, element)
            should_swap = self.should_swap(idx)

    def kthLargest(self, k, nums):
        self.k = k
        self.nums = nums
        kth_largest = self.heapify_up()
        return kth_largest

    def add(self, val: int) -> int:
        self.nums.append(val)
        kth_largest = self.heapify_up()
        return kth_largest



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

    testcase = [[4, [7, 7, 7, 7, 8, 3]], 2, 10, 9, 9]
    obj = KthLargest(*testcase[0])
    param_1 = obj.add(testcase[1])
    param_2 = obj.add(testcase[2])
    param_3 = obj.add(testcase[3])
    param_4 = obj.add(testcase[4])