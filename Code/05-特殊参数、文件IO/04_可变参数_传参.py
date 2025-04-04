def average(*args):
    rst = 0
    for arg in args:
        rst += arg
        
    return rst / len(args)

arr = [2,4,6,8]
print(average(2,4,6,8))
# 解包操作
print(average(*arr))
print(average(*[2,4,6,8]))


def show_info(**kwargs):
    print(kwargs)
    
stu = {
    "name": "李四光", 
    "age": 22, 
    "score":44.0
}
show_info(name="李四光", age=22, score=44.0)
# 解包操作
stu["age"] = 12
show_info(**stu)