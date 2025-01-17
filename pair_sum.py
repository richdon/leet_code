def pair_sum(sorted_list: list[int], target):
    left, right = 0, len(sorted_list) - 1
    pairs = []
    for _ in range(len(sorted_list) - 1):
        my_sum = sorted_list[left] + sorted_list[right]
        if my_sum == target:
            pairs.append([left, right])
        elif my_sum <= target:
            left += 1
        else:
            right -= 1
    return pairs


if __name__ == "__main__":
    tests = [
        [
            ([-5, -2, 3, 4, 6], 7),
            [[2, 3]]
        ],

        [
            ([], 0),
            []
        ],

        [
            ([1], 1),
            []
        ],

        [
            ([2, 3], 5),
            [[0, 1]]
        ],
        [
            ([2, 4], 5),
            []
        ],
        [
            ([2, 2, 3], 5),
            [[0, 2], [1, 2]]
        ],
        [
            ([-1, 2, 3], 2),
            [[0, 2]]
        ],

        [([-3, -2, -1], -5),
         [0, 1]]
    ]
    for test in tests:
        actual = pair_sum(*test[0])
        expected = test[1]
        assert actual == expected
