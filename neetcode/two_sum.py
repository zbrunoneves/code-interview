def two_sum(nums: list[int], target: int) -> list[int]:
    h = {}
    for i, n in enumerate(nums):
        diff = target - n
        if diff in h:
            return [h[diff], i]
        h[n] = i

    return []