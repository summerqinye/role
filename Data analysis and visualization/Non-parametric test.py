import scipy.stats as ss
import pandas as pd
from scipy.stats import spearmanr
df1 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\opportunistic.xlsx", sheet_name="indoor")
df2 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\algorithmic.xlsx", sheet_name="indoor")
df3 = pd.read_excel("C:\\Users\\lenovo\\Desktop\\paper\\collaborative.xlsx", sheet_name="indoor")


# 两种优化算法得到的结果是否有显著差异
# p1 < 0.05 ：说明拒绝原假设H0，接受备择假设H1，结论是x和y有显著差异
a = df1['Coverage']
b = df2['Coverage']
c = df3['Coverage']
# d = df4['efficiency']
print(list(a))
print(list(b))
print(list(c))


# 非参数检验，显著性检验

stats_m, p_m = ss.mannwhitneyu(a, b, alternative='two-sided')
print('p_m:', p_m)

stats_m1, p_m1 = ss.mannwhitneyu(a, c, alternative='two-sided')
print('p_m1:', p_m1)

stats_m2, p_m2 = ss.mannwhitneyu(b, c, alternative='two-sided')
print('p_m2:', p_m2)

# stats_m3, p_m3 = ss.mannwhitneyu(b, c, alternative='two-sided')
# print('p_m3:', p_m3)
#
# stats_m4, p_m4 = ss.mannwhitneyu(b, d, alternative='two-sided')
# print('p_m4:', p_m4)
#
# stats_m5, p_m5 = ss.mannwhitneyu(c, d, alternative='two-sided')
# print('p_m5:', p_m5)
# wilcoxon秩和检验的原假设（H0）是两组数据来自相同的分布（即两组数据没有显著差异）。对应的备择假设（H1）为两组数据中的有一组比另一组大（即两组数据存在显著差异）。
stats1, p1 = ss.ranksums(b, c, alternative='two-sided')
print('p1:', p1)
# p2 > 0.05：说明接受原假设H0，拒绝备择假设H1，结论是x不是比y大
# stats2, p2 = ss.ranksums(y, z, alternative='greater')
# p3 < 0.05：说明拒绝原假设H0，接受备择假设H1，结论是x比y小
# stats3, p3 = ss.ranksums(y, z, alternative='less')
# print('p2:', p2)
# print('p3:', p3)
