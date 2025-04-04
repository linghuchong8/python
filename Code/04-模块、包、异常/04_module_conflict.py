from hello import name as hello_name
from hi import name as hi_name
# 后导入的变量、函数、类会覆盖先导入的内容
# 解决方式1：通过as，起一个别名

print(hello_name)
print(hi_name)
