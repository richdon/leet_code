class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = [self.add(n) for n in nums]

    def get_parent_idx(self, i):
        return i // 2

    def get_right_child_idx(self, i):
        return 2 * i + 1

    def get_left_child_idx(self, i):
        return 2 * i + 2

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
        while self.should_swap(idx):
            element = self.nums[idx]
            idx = self.swap(idx, element)

    def kthLargest(self, k, nums):
        self.k = k
        self.nums = nums
        self.heapify_up()
        return self.check_kth_largest()

    def check_kth_largest(self):
        j = len(self.nums)
        idx = 0
        while j > idx and j != self.k:
            left_child = self.nums[self.get_left_child_idx(idx)]
            right_child = self.nums[self.get_right_child_idx(idx)]
            val = self.nums[idx]
            if left_child > val or right_child >

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.heapify_up()
        return self.check_kth_largest()


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
if __name__ == "__main__":
    ...
