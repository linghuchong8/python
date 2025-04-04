"""
输入文件的名字，然后程序自动完成对文件进行备份
1.输入文件名 b.py (如果文件不存在, 一直输入)
2.创建文件  文件名[复制].py
    文件名  [复制]  .py
    icheima.com[复制].py
3.读取文件, 写入到复制的文件中
"""
import os

file_name = None

while True:
    file_name = input("请输入文件名:")

    # 文件存在, 则结束循环
    if os.path.exists(file_name):
        break
    
    # 不存在, 提示用户, 继续循环
    print("文件不存在:", file_name)
    
# 查找.的位置, 生成新的文件名
dot_pos = file_name.rfind(".")
name_prefix = file_name[:dot_pos]
name_suffix = file_name[dot_pos:]
new_file_name = f"{name_prefix}[复制]{name_suffix}"
print(f"开始拷贝文件: {file_name} -> {new_file_name}")

content = None
# 读取原有文件 binary, byte, bit
with open(file_name, "rb") as old_file:
    content = old_file.read()
    
# print(type(content))
# print(content)
# content = b'\xe6\x88\x91\xe6\x9c\x89\xe4\xb8\x80\xe4\xb8\xaa\xe6\xaf\x9b\xe8\xa1\xab1\r\n\xe6\x98\xbe\xe5\xbe\x97\xe5\xbe\x88\xe5\xbf\xa0\xe8\xaf\x9a2\r\n\xe6\x9c\x9b\xe5\xba\x90\xe5\xb1\xb1\xe7\x80\x91\xe5\xb8\x833\r\n'
    
# 将内容写出到新文件 binary, byte, bit
with open(new_file_name, "wb") as new_file:
    new_file.write(content)
    
print("拷贝完成")