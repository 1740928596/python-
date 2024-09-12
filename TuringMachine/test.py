from TuringMachine import TuringMachine

tm_add = TuringMachine('test.tr')
tm_add.run('')
# 获取运行结果长度并打印
result = len(tm_add.getTuringResult())

print('TM: 3+5={0}'.format(result))


