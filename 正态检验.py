import matplotlib.pyplot as plt

# import math

# import seaborn as sns
import pandas as pd
import scipy

plt.rcParams['font.family'] = ['sans-serif']

plt.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.sans-serif'] = ['SimHei']

# df1 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\课件\\PPG-BP dataset.xlsx",index_col=None)
df1 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\random.xlsx", sheet_name="urban")
df2 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\aco.xlsx", sheet_name="urban")
# df3 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\dt.xlsx", sheet_name="open")
# df4 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\random.xlsx", sheet_name="natural")

def zhengtai(data):
    # 直方图

    # plt.hist(data, bins=10)
    #
    # plt.show()
    #
    # # QQ图
    #
    # import statsmodels.api as sm
    #
    # import pylab
    #
    # sm.qqplot(data, line='s')
    #
    # pylab.show()

    # 偏度峰度检验，axis：默认为0，表示在0轴上检验，即对数据的每一行做正态性检验，我们可以设置为 axis=None 来对整个数据做检验

    # nan_policy：当输入的数据中有空值时的处理办法。默认为 ‘propagate’，返回空值；设置为 ‘raise’ 时，抛出错误；设置为 ‘omit’ 时，在计算中忽略空值。

    from scipy.stats import normaltest

    '''输出结果中第一个为统计量，第二个为P值（注：p值大于显著性水平0.05，认为样本数据符合正态分布）'''

    print('偏度峰度检验', normaltest(data, nan_policy='propagate'))

    # KS检验

    from scipy.stats import kstest

    '''输出结果中第一个为统计量，第二个为P值（注：统计量越接近0就越表明数据和标准正态分布拟合的越好，

    如果P值大于显著性水平，通常是0.05，接受原假设，则判断样本的总体服从正态分布）'''

    # cdf中可以指定要检验的分布，norm表示我们需要检验的是正态分布

    # 常见的分布包括norm,logistic,expon,gumbel等

    print('KS检验', kstest(data, cdf="norm"))

    # w检验

    '''输出结果中第一个为统计量，第二个为P值（统计量越接近1越表明数据和正态分布拟合的好，

    P值大于指定的显著性水平，接受原假设，认为样本来自服从正态分布的总体）'''

    from scipy.stats import shapiro

    print('w检验', shapiro(data))

    # aderson检验
    '''如果检验统计量高于临界值，则在相应的显着性水平上拒绝零假设
    （即，有证据表明总体不遵循该特定分布）'''

    from scipy.stats import anderson

    print('anderson检验', anderson(data))
    #



# # 变化为正态性，BOXCOX
# print('正态检验1')
# zhengtai(df3['Coverage'])
# print('正态检验2')
# # zhengtai(df3['intervention'])
# print('正态检验3')
zhengtai(df2['efficiency'])
# print('正态检验4')
zhengtai(df1['efficiency'])

#from scipy import stats
# data1, la = stats.boxcox(df1['优化前'], lmbda=None, alpha=None)  # 将数据进行BOX-COX变换
# zhengtai(data1)
from scipy.stats import levene, spearmanr


# 方差齐性检验
print('方差齐性检验')
'"当检验统计量在拒绝域中时，P值小于显著性水平；检验统计量未落在拒绝域中时，P值大于显著性水平。p>0.05,表明二者具有方差齐性"'
a = df1['efficiency'] # Coverage, efficiency
b = df2['efficiency'] # Coverage, efficiency
stat, p = levene(a, b)
print("stat=", stat)
print("p=", p)

# Example of the Spearman's Rank Correlation Test，用于独立性检验
stat, p = spearmanr(b, a)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
    print('Probably independent')
else:
    print('Probably dependent')
print('student-t 检验')
# Example of the Student's t-test
from scipy.stats import ttest_ind
#
stat, p = ttest_ind(a, b)
print(stat, p)
if p > 0.05:
    print('Probably the same distribution')
else:
    print('Probably different distributions')


print('修正student-t 检验')
stat, p = ttest_ind(a, b, equal_var=False)
print(stat, p)
if p > 0.05:
    print('修正检验，Probably the same distribution')
else:
    print('修正检验，Probably different distributions')
