'''
19. 計算有幾個英文單字
輸入一個只包含英文字和空白的字串，你的函式能找出這個字串中有幾個英文單字。

不考慮英文單字是否真的存在，且假設英文單字間用一個空白隔開，字串的前後有可能包含零到多個空白。

輸入範例一："Today is a good day"
回傳：5

輸入範例二：" My name is John"
回傳：4

輸入範例一：" Good "
回傳：1

輸入範例一：" "
回傳：0
'''

"""
    @param s:{String}
    @return :{Integer}
"""
def countWords(s):
    # 你的程式碼
    words = s.strip().split()
    return len(words)

# strip: to remove any leading, and trallling whitespaces
# leading: at the beginning of the string
# trailling: at the end
# https://www.w3schools.com/python/ref_string_strip.asp

# split: to split a string into a list
# https://www.w3schools.com/python/ref_string_split.asp

# len: to return the number of items in an object
# https://www.w3schools.com/python/ref_func_len.asp