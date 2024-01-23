'''
4. 找到第二大的整數
輸入包含至少兩個不同整數的陣列 / 列表，找到並回傳其中第二大的整數。

輸入範例一：[1, 3, 3, 2, 5, -2]
回傳：3

輸入範例二：[-5, -10, -8, 1, -1]
回傳：-1

輸入範例一：[0, 2]
回傳：0
'''

"""
    @param nums:{[Integer]}
    @return :{Integer}
"""
def findSecond(nums):
    # 你的程式碼
    max_num = 0
    sec_num = 1

    for i in range(len(nums)):
        if nums[i] > nums[max_num]:
            sec_num = max_num
            max_num = i 
        elif nums[i] > nums[sec_num] and nums[i] < nums[max_num]:
            sec_num = i
        
    return nums[sec_num]

'''
solution
    - Initialize variables to track the maximum and second maximum numbers
    - Check if the current element is greater than the current max_num
        - if Ture, Update max_num to the current index
    - Check if the current element is greater than the current second_max and less than the current max_num
        - if Ture, Update second_max to the current index
reference
    - https://www.freecodecamp.org/news/python-range-function-example/
'''