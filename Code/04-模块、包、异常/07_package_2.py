# 2. 通过 from 包名 import 模块名

from pkg import hello

# 变量
print(hello.name)

# 函数
hello.say()

# 类
print(hello.Nice().name)