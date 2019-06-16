import numpy as np
import scipy as sp
import pydotplus
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

# 读入数据
data = []
labels = []
with open("data.txt") as ifile:  
        for line in ifile:  
            tokens = line.strip().split(' ')  
            data.append([float(tk) for tk in tokens[:-1]])  
            labels.append(tokens[-1])  
x = np.array(data)
labels = np.array(labels)
y = np.zeros(labels.shape)


# 胖瘦类别数字化
y[labels=='fat']=1
# 数据拆分，80%训练，20%测试
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size = 0.2,random_state=0)

# 使用DecisionTreeClassifier建立模型并训练
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(x_train, y_train)

# 测试结果
answer = clf.predict(x_train)
print("训练的样本数据:\n ", x_train) # 训练样本数据
print("训练结果: ", answer)   
print("实际结果: ", y_train)  # 训练样本类别
print("准确率: ", np.mean( answer == y_train))

print("影响比例: 身高-体重\n", clf.feature_importances_)

# 保存决策树为dot文件，后续图形处理
with open("tree.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
