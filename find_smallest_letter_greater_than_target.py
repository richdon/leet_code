def nextGreatestLetter(letters: list[str], target: str) -> str:
    left_ptr, right_ptr = 0, len(letters)-1
    while left_ptr <= right_ptr:
        mid = (left_ptr + right_ptr) // 2
        if target < letters[mid]:
            right_ptr = mid - 1
        else:
            left_ptr = mid + 1
    return letters[left_ptr % len(letters)]


if __name__ == "__main__":
    print(nextGreatestLetter(["x", "x", "y", "y"], "z"))
