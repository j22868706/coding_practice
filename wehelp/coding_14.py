'''
14. 整數陣列 / 列表中，兩兩相乘的最大值
輸入一個至少包含兩個整數的陣列 / 列表，其中可能包含重複的數字if，你的函式能算出並回傳兩兩數字相乘後最大的乘積。

輸入範例一：[2, -1, 0]
回傳：0

輸入範例二：[-2, -10, 1, 2]
回傳：20

輸入範例一：[3, 1, 9, 4, 5]
回傳：45
'''

"""
    @param nums:{[Integer]}
    @return :{Integer}
"""
def findMaxProduct(nums):
    # 你的程式碼
    nums.sort()
    if nums[0] * nums[1] > nums[-1] * nums[-2]:
        return nums[0] * nums[1]
    else:
        return nums[-1] * nums[-2]

# This function sorts the list and then finds the maximum result by comparing the products of the first two numbers 
# and the last two numbers.
# https://www.w3schools.com/python/ref_list_sort.asp
