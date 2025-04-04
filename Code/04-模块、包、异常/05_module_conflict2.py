import hello 
import hi   
# 后导入的变量、函数、类会覆盖先导入的内容
# 解决方式1：通过as，起一个别名
# 解决方式2: 整体导入

print(hello.name)
print(hi.name)

hello.say()
print(hello.Nice().name)

