# Python code​​​​​​‌​‌​‌​​​​​​​‌‌‌‌​‌​‌​​​​​ below
# Use print("messages...") to debug your solution.
show_expected_result = False
show_hints = True

def is_palindrome(teststr):
    lowteststr = teststr.lower()
    newstr = ""
    for c in lowteststr:
        if c.isalnum():
            newstr += c

    if newstr == newstr[::-1]:
        return True
    return False
