import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
df = pd.read_excel('C:\\Users\\lenovo\\Desktop\\paper\\方差分析.xlsx')
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm


print("***********coverage-ANOVA***********")
model = ols('coverage~ strategy + environment+ strategy:environment', data=df[['strategy', 'environment', 'coverage']]).fit()
anovat = anova_lm(model)
# print(model.summary())
print(anovat)

print()
print("***********efficiency-ANOVA***********")
model1 = ols('efficiency~ C(strategy) + C(environment)+ C(strategy):C(environment)', data=df[['strategy', 'environment', 'efficiency']]).fit()
anovat1 = anova_lm(model1)
# print(model.summary())
print(anovat1)

print()
print("***********frequency-ANOVA***********")
model2 = ols('frequency~ C(strategy) + C(environment)+ C(strategy):C(environment)', data=df[['strategy', 'environment', 'frequency']]).fit()
anovat2 = anova_lm(model2)
# print(model.summary())
print(anovat2)
