

#This was too slow, time limit exceeded
# def shift_left_on(nums: List[int], index: int, length: int):
#     while index < length:
#         nums[index] = nums[index+1]
#         index = index + 1
#
#
#
# def remove_duplicates(nums: List[int]) -> int:
#     length = len(nums)
#     previous = 'unset'
#     iter1 = 0
#
#     while iter1 < length:
#         if nums[iter1] == previous:
#             shift_left_on(nums, iter1, length-1)
#             length = length - 1
#         else:
#             previous = nums[iter1]
#             iter1 = iter1 + 1
#
#     return length

#from solution, still very slow
def remove_duplicates(nums: List[int]) -> int:

    length = len(nums)

    if length == 0:
        return 0

    insert_index = 1

    for i in range(1, length):
        if nums[i] != nums[i - 1]:
            nums[insert_index] = nums[i]
            insert_index = insert_index + 1

    return insert_index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    numbers = [1, 2, 2, 3, 3, 3, 4]

    print(remove_duplicates(numbers))
    print(numbers)
