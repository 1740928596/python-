T = int(input())
stack1 = []
stack2 = []
for i in range(T):
    list_in = input().split()
    # print(list_in[0])
    if list_in[0] == 'I':
        stack1.append(int(list_in[1]))
    else:
        if len(stack1) == 0 and len(stack2) == 0:
            print("ERROR")
        elif len(stack1) != 0 and len(stack2) == 0:
            stack1.reverse()
            stack2 = list(stack1)
            stack1.clear()
            L = 2*len(stack2)+1
            print(stack2.pop(),L)
        else:
            print(stack2.pop(),1)