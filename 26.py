def count_words():
    # 读取输入的行数
    n = int(input())
    
    # 存储结果的列表
    results = []
    
    # 逐行读取输入并计算单词数量
    for _ in range(n):
        line = input().strip()
        word_count = len(line.split())
        results.append(word_count)
    
    # 打印每行的单词数量
    for count in results:
        print(count)

# 调用函数执行
count_words()
