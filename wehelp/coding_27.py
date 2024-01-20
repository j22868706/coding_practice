'''
27. 檢查兩個區間是否重疊
輸入兩個陣列 / 列表，分別代表兩個整數區間的最小值和最大值 [min1, max1] 和 [min2, max2]，你的函式能判斷兩個整數區間是否重疊，包含最小或最大值落在同一個整數的狀況。

可以假設每個區間的最大值一定大於最小值。

輸入範例：[5, 10]，[9, 11]
回傳：真

輸入範例：[-5, 5]，[8, 10]
回傳：假

輸入範例：[-5, 5]，[-6, -5]
回傳：真
'''

"""
    @param range1:{[Integer]}
    @param range2:{[Integer]}
    @return :{Boolean}
"""
def isOverlapping(range1, range2):
    # 你的程式碼
    x = len(range1) - 1
    y = len(range2) - 1
    
    if range2[0] <= range1[0] <= range2[y]:
        return True
    elif range2[0] <= range1[x] <= range2[y]:
        return True
    elif range1[0] <= range2[0] <= range1[x]:
        return True
    elif range1[0] <= range2[y] <= range1[x]:
        return True
    else:
        return False
    
# Note: 
    # checks for overlapping ranges
    # Python len() function
    # https://www.w3schools.com/python/ref_func_len.asp