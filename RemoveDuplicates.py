# python script to remove duplicates
def contains_duplicate(nums):
    final_arr = []
    for i in nums:
        if i not in final_arr:
            final_arr.append(i)
    return len(final_arr) != len(nums)

nums = list(map(int, input().split()))
print(contains_duplicate(nums))