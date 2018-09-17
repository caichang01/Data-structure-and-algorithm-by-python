# 快速排序实现
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # 左子数组
    left = []
    # 右子数组
    right = []
    # 基准数
    base = nums.pop()

    # 遍历，分别进入左和右子数组
    for x in nums:
        if x <= base:
            left.append(x)
        else:
            right.append(x)

    # 递归调用
    left = quicksort(left)
    left.append(base)
    answerlist = left + quicksort(right)

    return answerlist


# 插入排序
def insertsort(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    return nums


# 冒泡排序
def bubbleSort(nums):
    passnum = len(nums)
    for i in range(passnum):
        for j in range(passnum - i - 1):
            # 左右相邻元素，按大在右，小在左进行交换，确保最大的在最右侧
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp
    return nums


if __name__ == '__main__':
    nums = [1, 5, 7, 6, 4, 9, 2]
    print(quicksort(nums))
    nums = [1, 5, 7, 6, 4, 9, 2]
    print(bubbleSort(nums))
    nums = [1, 5, 7, 6, 4, 9, 2]
    print(insertsort(nums))
