from TuringMachine import TuringMachine

# 定义读取函数
def ru(file,operators,i,j):
    file.write(f'1,{operators[i]},{operators[j]}\n')

def busyBeaver(nState):
    # 定义最大循环次数
    max_index = 2 * (nState + 1)
    # 初始化busyBeaver数为0
    result = 0
    # 初始化执行步数为0
    steps = 0
    # 保存所有可能操作的列表
    operators = []
        
    # 遍历所有可能的操作组合，bb1与bb2写入默认设为1
    for opt1 in ['L','R']:
        i = 0
        for opt2 in range(max_index):
            operators = operators + [f'{1}{opt1}{opt2}']
            i+=1

    # 对于每一种操作组合，进行遍历
    i = 0
    while i < max_index:
        j = 0
        while j < max_index:
            # 计算bb1
            if nState == 1:
                with open('cache.txt', 'w+') as B:
                    ru(B, operators,i,j)
                classTu = TuringMachine('cache.txt')
                try:
                    temp_0 = int(classTu.run(''))
                except:
                    j += 1
                    continue
                temp_1 = classTu.getTuringResult()
                if temp_1 > result:
                    result = temp_1
                    steps = temp_0
            # 计算bb2
            elif nState >= 2:
                l = 0
                while l < max_index:
                    k = 0
                    while k < max_index:
                        with open('cache.txt', 'w+') as B:
                            ru(B, operators,i,j)
                            ru(B, operators,l,k)
                        classTu = TuringMachine('cache.txt')
                        try:
                            temp_0 = int(classTu.run(''))
                        except:
                            k += 1
                            continue
                        temp_1 = classTu.getTuringResult()
                        if temp_1 > result:
                            result = temp_1
                            steps = temp_0
                        k += 1
                    l += 1
            j += 1
        i += 1


    # 尝试bb3
    i, j, k, l, m, n = 0, 0, 0, 0, 0, 0
    
# 去掉注释后可尝试运行，但超出限度返回0
    '''while i < max_index:
        j = 0
        while j < max_index:
            k = 0
            while k < max_index:
                l = 0
                while l < max_index:
                    m = 0
                    while m < max_index:
                        n = 0
                        while n < max_index:
                            if i or j or k or l or m or n >= len(operators):
                                n += 1
                                continue
                            with open('cache.txt', 'w+') as B:
                                ru(B, operators, i, j)
                                ru(B, operators, k, l)
                                ru(B, operators, m, n)
                            classTu = TuringMachine('cache.txt')
                            try:
                                temp_0 = int(classTu.run(''))
                            except:
                                n += 1
                                continue
                            temp_1 = classTu.getTuringResult()
                            if temp_1 > result:
                                result = temp_1
                                steps = temp_0
                            n += 1
                        m += 1
                    l += 1
                k += 1
            j += 1
        i += 1'''


    print("busy beaver%d steps is:%d " %(nState,steps))#输出图灵机执行步数，有些文章中定义这是bb(n)                   
    return result


# 主函数
if __name__ == '__main__':
    # 初始化一个加法图灵机并运行
   
    tm_add = TuringMachine('add.tr')
    tm_add.run('111011111')
    # 获取运行结果长度并打印
    tm_add.visualize()
    result = tm_add.getTuringResult()
   
    print('TM: 3+5={0}'.format(result))

    # 初始化一个乘法图灵机并运行
    tm_multiply_two = TuringMachine('multiply_two.tr')
    tm_multiply_two.run('11111')

    result = tm_multiply_two.getTuringResult()
    print('TM: 5x2={0}'.format(result))

    # 初始化一个加法图灵机并运行
    tm_plus_three = TuringMachine('plus_three.tr')
    tm_plus_three.run('11111')

    result = tm_plus_three.getTuringResult()
    print('TM: 5+3={0}'.format(result))

    tm_multiply_two_plus_three = TuringMachine('multiply_two_plus_three.tr')
    tm_multiply_two_plus_three.run('11111')

    result = tm_multiply_two_plus_three.getTuringResult()
    print('TM: 2x5+3={0}'.format(result))
    tm_multiply_two_plus_three.visualize()

    # 计算1状态
    B1Number = busyBeaver(1)
    print('Busy Beaver Number for 1 state is: {0}.'.format(B1Number))

    # 计算2状态
    B2Number = busyBeaver(2)
    print('Busy Beaver Number for 2 states is: {0}.'.format(B2Number))

    # 计算3状态
    B3Number = busyBeaver(3)
    print('Busy Beaver Number for 3 states is: {0}.'.format(B3Number))
