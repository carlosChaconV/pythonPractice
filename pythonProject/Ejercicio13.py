
numbers = [5,6,4,1,10]


def nearFirst(nums):
    near = max(nums)
    for i in range(len(nums) - 1):
        if abs(nums[0] - nums[i+1]) < near:
            near = nums[i+1]

    print(f'el numero mas cercano al {nums[0]} es el {near}')


nearFirst(numbers)


