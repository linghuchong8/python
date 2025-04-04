"""
需求
一个学校，有3个办公室，现在有8位老师等待工位的分配
['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']

请编写程序:
1. 完成随机的分配
2. 打印办公室信息 (每个办公室中的人数，及分别是谁)

#进阶：保证每个办公室至少一人
"""
import random
offices = [
    [], # 0
    [], # 1
    [], # 2
]

teachers = ['袁腾飞', '罗永浩', '俞敏洪', '李永乐', '王芳芳', '马云', '李彦宏', '马化腾']

# 1. 完成随机的分配 。 让所有人排好队，逐个抽签0, 1, 2

# 遍历每个老师
for teacher in teachers:
    # 生成随机数[0, 1, 2]
    office_id = random.randint(0, 2)
    # 将老师请到对应办公室
    offices[office_id].append(teacher)
    
# 2. 打印办公室信息 (每个办公室中的人数，及分别是谁)
for office in offices:
    # 获取每个房间的人数
    count = len(office)
    print("房间人数：{} 列表：{}".format(count, office))