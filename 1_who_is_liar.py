print("game:谁是说谎者\n"
    "规则：\n",
    "用0代表说谎者，用1代表诚实者，\n"
    "如01代表A是说谎者，B是诚实者，11代表两个人都是诚实者\n，"
    "A与B的所有陈述都可以转换为各种情况，如A说B在撒谎，等价于10 00\n"
    "B说我们是不同的人等价于10 01"
    "demo:"
    "请输入A的陈述:10 11 (我不是说谎者)\n"
    "请输入B的陈述:10 01(我们是不同种的人)"
    "结果A和B分别为10")

while 1:
    A = set(map(int,input("请输入A的陈述").split()))
    B = set(map(int,input("请输入B的陈述").split()))
    set_c= A&B
    list_c= list(set_c)
    if len(list_c)!=1:
        print("逻辑错误")
        continue
    print("%d" %list_c[0])

    if input("还想再玩吗? 输y再玩一次，按其它键退出")=='y':
        continue
    else:
        print("感谢游玩")
        break