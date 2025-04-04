"""
关键字可变参数
kw -> key word
"""

def key_word_args(**kwargs):
    # 所有的参数被打包成字典
    print(kwargs, type(kwargs))
    # print(**kwargs)
    print(kwargs["name"])
    print(kwargs["height"])
    print(kwargs["age"])

key_word_args(name="ZhangSan", age=87, height=165.3)

def key_word_args1(id, **kwargs):
    # 所有的参数被打包成字典
    print(kwargs, type(kwargs))
    # print(**kwargs)
    print(id)
    print(kwargs["name"])
    print(kwargs["height"])
    print(kwargs["age"])

key_word_args1(123, name="ZhangSan", age=87, height=165.3)