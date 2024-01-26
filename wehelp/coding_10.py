'''
10. 用前一個有效值填滿空字串
輸入一個可能包含空字串的字串陣列 / 列表，你的函式能把陣列 / 列表中的空字串用前一個有效值 ( 非空字串 ) 取代。若沒有前一個有效值，則保持空字串不變。

輸入範例一：["", "a", "", "", "c"]
回傳：["", "a", "a", "a", "c"]

輸入範例二：["a", "b", "", "c", ""]
回傳：["a", "b", "b", "c", "c"]

輸入範例一：["", "", "a"]
回傳：["", "", "a"]
'''

"""
    @param words:{[String]}
    @return :{[String]}
"""
def ffill(words):
    # 你的程式碼
    previous_value = None

    for i in range(len(words)):
        if words[i] != "":
            previous_value = words[i]
        elif previous_value is not None:
            words[i] = previous_value
    return words

'''
- Solution
    1. Inside the loop, it checks if the current element is not an empty string using if words[i] != "".
        If true, it updates the previous_valid_value with the current non-empty string.
    2. If the current element is an empty string and there is a previous_valid_value
        (checked using elif previous_valid_value is not None), 
        it replaces the empty string with the previous_valid_value.
'''