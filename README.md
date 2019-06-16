# 数据挖掘算法
1. [关联分析Apriori算法](#关联分析Apriori算法)  
2. [数据分类决策树算法](#数据分类决策树算法)
3. [数据聚类K-means算法](#数据聚类K-means算法)
  

<hr>

## 关联分析Apriori算法
### 1. [数据集](关联分析（Apriori）/data.txt)  
以超市交易为数据集，所有商品的项集为        
*I = {bread, beer, cake, cream, milk, tea}*  
某条交易如  
*Ti = {bread, beer, milk}*   
简化为  
*Ti = {a, b, d}*  
data.txt数据集样本如下
```bash
a, d, e,f
a, d, e
c, e
e, f
...
```

### 2. [算法实现](关联分析（Apriori）/correlation_analysis.py)
使用经典的Apriori算法，依次扫描交易记录集，计算出 *k-候选集Ck* 然后去除**支持度sup**小的项集获得 *k-频繁集Lk*， 只计算到 *3-频繁集* 
> 第k个候选集只会从k-1频繁集中的各项目组合连接，然后扫描记录集，以获取Ck中各项集的支持度。    

![输出结果](https://i.loli.net/2019/06/16/5d05ad0e8f2e762317.png)


## 数据分类决策树算法







## 数据聚类K-means算法