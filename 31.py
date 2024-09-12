stack = []
k = ""
a = True
while a:
    list1 = input()
    if list1[0] == ".":
        break

    for key,i in enumerate(list1):
        if i == "(":
            stack.append("(")
        elif i == ")":
            if len(stack) == 0:
                stack.append(i)
                a = False
                break
            k = stack.pop()
            if k != "(":
                break

        elif i == "{":
            stack.append("{")
        elif i == "}":
            if len(stack) == 0:
                stack.append(i)
                a = False
                break
            k = stack.pop()
            if k != "{":
                break

        elif i == "[":
            stack.append("[")
        elif i == "]":
            if len(stack) == 0:
                stack.append(i)
                a = False
                break
            k = stack.pop()
            if k != "[":
                break

        elif i == "*" and list1[key-1] == "/":
            stack.append("/*")
        elif i == "*" and list1[key + 1] == "/":
            if len(stack) == 0:
                stack.append(i)
                a = False
                break
            k = stack.pop()
            if k != "/*":
                break





if k != "":
    print(f"NO\n{k}-?")

elif k == "" and len(stack) > 0:
    print(f"NO\n?-{stack.pop()}")

else:
    print("YES")
