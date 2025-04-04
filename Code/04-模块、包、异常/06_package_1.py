# 1.直接通过 包名.模块名 访问内容
import pkg.hello

print(pkg.hello.name)
pkg.hello.say()

print(pkg.hello.Nice().name)