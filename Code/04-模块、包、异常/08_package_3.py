# 3. from 包名.模块名 import 变量，函数，类

from pkg.hello import name, say
from pkg.hello import Nice

# 变量
print(name)

# 函数
say()

# 类
print(Nice().name)