'''
8. 計算等差數列的總和
輸入等差數列中最小的整數、最大的整數、以及公差，計算數列中每個數字的總和。可以假設輸入的最大數字一定大於最小數字。

輸入範例一：最小 2、最大 8、公差 2，計算 2+4+6+8 的總和
回傳：20

輸入範例二：最小 -2、最大 3、公差 1，計算 (-2)+(-1)+0+1+2+3 的總和
回傳：3

輸入範例一：最小 10、最大 14、公差 3，計算 10+13 的總和
回傳：23
'''

"""
    @param min:{Integer}
    @param max:{Integer}
    @param differ:{Integer}
    @return :{Integer}
"""
def sumOfArithmeticSequence(min, max, differ):
    # 你的程式碼
    total = 0
    for i in range(min, max+1, differ):
        total += i
    return total

# solution
    # https://www.w3schools.com/python/python_for_loops.asp