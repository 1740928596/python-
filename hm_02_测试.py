def list_test():
    """列表测试"""
    name_21_list = ["贾", '刘', '米']
    name_22_list = ["张", "米", '廖']
    name_21_list.extend(name_22_list)
    print(name_21_list)


def variable_plus_string_test():
    """变量与字符叠加测试"""
    # (一)变量含义为字符时
    a = "米俊阳"
    # 1.直接堆叠
    # print(a"好帅")
    # 报错

    # 2.加号连接
    print("第一个 " + a + "好帅")
    # 运行结果米俊阳好帅

    # 3.乘号连接
    # 报错can't multiply sequence by non-int of type 'str' 无法将序列与“str”类型的非int相乘

    # (二)变量含义为数据时
    b = 2
    # 整数
    # 1.直接堆叠
    # print(b"米俊阳")
    # 报错bytes can only contain ASCII literal characters. 字节只能包含ASCII文字字符。

    # 2.加号连接
    # print(b+"米俊阳")
    # 报错unsupported operand type(s) for +: 'int' and 'str' 不支持+：“int”和“str”的操作数类型

    # 3.乘号连接
    print("第二个 " + b * '米俊阳 ', )
    # 连续输出b=2个米俊阳
    # 经测试得字符后面像元组一样加个逗号不会有影响

    # 非整数
    # 1.浮点型
    c = 0.1
    # print(c * '米俊阳 ', )
    # 报错can't multiply sequence by non-int of type 'float' 无法将序列与“float”类型的非int相乘

    # 2.布尔型
    d = True
    # d = False
    print("第三个 " + d * '米俊阳 ', )
    # 有意思
    # d与米俊阳相乘,当d为真时,米俊阳没变化,当d 为假时,米俊阳此字符会消失

    # 相加
    # print("第四个 " + d + "米俊阳")
    # 报错can only concatenate str (not "bool") to str 只能将str（而不是“bool”）连接到str
    # 由此可见+ 表示连接

    # (三)变量为列表时
    e = [1, 2, 3, 4, ]
    # 同样,定义列表时多一个逗号不会影响,多两个会报错
    # 1.加号连接
    # print(a + "米俊阳")
    # 报错 can only concatenate list (not "str") to list 只能将列表（而不是“str”）连接到列表
    # 之后不用再试了,+号只适用于字符与字符连接

    # 2.乘号连接
    # print(a * "米俊阳")
    # 报错can't multiply sequence by non-int of type 'str' 无法将序列与“str”类型的非int相乘

    # 其余不用再试了
