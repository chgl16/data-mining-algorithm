import random
with open('data_lab2.txt', 'w') as f:
    # f.write('height\tweight\n')
    # 生成300个随机数
    for i in range(300):
        height = random.randint(1600, 1900) / 10
        weight = (height - 100) * 0.9 + random.randint(-50, 50) / 10
        #标准体重＝0.9*身高－90
        flag = 0.9 * height - 90
        if (flag < weight):
            p = "fat"
        else:
            p = "thin"
        f.write('%d %d %s\n' % (height, weight, p))
        
