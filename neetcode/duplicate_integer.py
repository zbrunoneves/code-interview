def has_duplicate(nums: list[int]) -> bool:
    h = {}
    for n in nums:
        if n in h:
            return True
        h[n] = None

    return False