# Python code​​​​​​‌​‌​‌​​​​​‌‌​‌‌‌‌​‌​‌​​​​ below
# Use print("messages...") to debug your solution.
import os
from os import path

show_expected_result = False
show_hints = False


def file_info():
    totalbytes = 0
    src = "deps" 
    
    for item in os.listdir(src): #获取deps目录下的所有文件
        item_path = os.path.join(src, item)
        if item.endswith(".txt") and os.path.isfile(item_path): #这一步在检查了endswith之后依然检查isfile的原因是，去除该目录下子目录中的txt文件
            totalbytes += os.path.getsize(item_path)
    
    return totalbytes
