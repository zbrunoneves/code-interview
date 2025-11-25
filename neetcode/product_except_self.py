def product_except_self(nums: list[int]) -> list[int]:
    lefts = {}
    rights = {}

    x = nums[0]
    for i in range(1, len(nums)):
        lefts[i]=x
        x *= nums[i]

    x = nums[-1]
    for i in range(len(nums)-2, -1, -1):
        rights[i] = x
        x *= nums[i]

    ans = []
    for i in range(len(nums)):
        ans.append(lefts.get(i, 1)*rights.get(i, 1))

    return ans