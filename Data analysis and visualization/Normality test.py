import matplotlib.pyplot as plt

# import math

# import seaborn as sns
import pandas as pd
import scipy

plt.rcParams['font.family'] = ['sans-serif']

plt.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.sans-serif'] = ['SimHei']


df1 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\opportunistic.xlsx", sheet_name="urban")
df2 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\algorithmic.xlsx", sheet_name="urban")


def zhengtai(data):

    from scipy.stats import shapiro

    print('w test', shapiro(data))

#from scipy import stats
# data1, la = stats.boxcox(df1['优化前'], lmbda=None, alpha=None)  # 将数据进行BOX-COX变换
# zhengtai(data1)
from scipy.stats import levene, spearmanr


# # 方差齐性检验
# print('方差齐性检验')
# '"当检验统计量在拒绝域中时，P值小于显著性水平；检验统计量未落在拒绝域中时，P值大于显著性水平。p>0.05,表明二者具有方差齐性"'
# a = df1['efficiency'] # Coverage, efficiency
# b = df2['efficiency'] # Coverage, efficiency
# stat, p = levene(a, b)
# print("stat=", stat)
# print("p=", p)

# # Example of the Spearman's Rank Correlation Test，用于独立性检验
# stat, p = spearmanr(b, a)
# print('stat=%.3f, p=%.3f' % (stat, p))
# if p > 0.05:
#     print('Probably independent')
# else:
#     print('Probably dependent')
# print('student-t 检验')
# # Example of the Student's t-test
# from scipy.stats import ttest_ind
# #
# stat, p = ttest_ind(a, b)
# print(stat, p)
# if p > 0.05:
#     print('Probably the same distribution')
# else:
#     print('Probably different distributions')


# print('修正student-t 检验')
# stat, p = ttest_ind(a, b, equal_var=False)
# print(stat, p)
# if p > 0.05:
#     print('修正检验，Probably the same distribution')
# else:
#     print('修正检验，Probably different distributions')
