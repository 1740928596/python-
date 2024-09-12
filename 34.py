str = input()
start,len = map(int,input().split())
str = (str[:start-1] + str[start-1+len:]).strip()
print(str)