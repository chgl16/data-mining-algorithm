# 数据挖掘算法
1. [关联分析Apriori算法](#关联分析Apriori算法)  
2. [数据分类决策树算法](#数据分类决策树算法)
3. [数据聚类K-means算法](#数据聚类K-means算法)
  

<hr>

## 关联分析Apriori算法
#### 1. [数据集](关联分析（Apriori）/data.txt)  
以超市交易为数据集，所有商品的项集为    
```bash    
I = {bread, beer, cake, cream, milk, tea}
```
某条交易如  
```bash
Ti = {bread, beer, milk}
```
简化为  
```bash
Ti = {a, b, d}
```
data.txt数据集样本如下
```bash
a, d, e,f
a, d, e
c, e
e, f
...
```

#### 2. [算法实现](关联分析（Apriori）/correlation_analysis.py)
使用经典的Apriori算法，依次扫描交易记录集，计算出 *k-候选集Ck* 然后去除**支持度sup**小的项集获得 *k-频繁集Lk*， 只计算到 *3-频繁集* ，最后计算管理规则可信度即可。
> 第k个候选集只会从k-1频繁集中的各项目组合连接，然后扫描记录集，以获取Ck中各项集的支持度。    

![输出结果](https://i.loli.net/2019/06/16/5d05ad0e8f2e762317.png)

<hr>

## 数据分类决策树算法
#### 1. [数据集](数据分类（决策树）/data.txt)
使用身高体重指数分为胖瘦两个分类，数据自己生成见 [*data_generation.py](数据分类（决策树）/data_generation.py) 比较简陋。  
数据集样本如下
```bash
184 77 fat
189 81 fat
178 75 fat
...
```

#### 2.[算法实现](数据分类（决策树）/decision_tree.py)
调用python实现的类库，比较简单
```python
from sklearn import tree
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

...

# 数据拆分，80%训练，20%测试
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size = 0.2,random_state=0)

# 使用DecisionTreeClassifier建立模型并训练
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf.fit(x_train, y_train)

...
```
打印后同时保持决策树到文件 [*tree.dot](数据分类（决策树）/tree.dot)，通过dot命令可以生产决策树图形（或者[在线转换](http://www.webgraphviz.com/)
```python
# 保存决策树为dot文件，后续图形处理
with open("tree.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
```
算法输出  
![算法输出](https://i.loli.net/2019/06/16/5d05b41f3cca371767.png)  
决策树
![决策树](https://i.loli.net/2019/06/16/5d05b41f6850332395.png)


## 数据聚类K-means算法