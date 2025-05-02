import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('docs.csv', delimiter="\t")

cases = cases_by_judge(df)
df_cases = pd.DataFrame(list(cases.items()), columns = ['judge', 'cases'])

top_10 = df_cases.nlargest(10, 'cases')
top_10.to_csv('diagram/top_10_judges.csv', encoding='utf-8', index=True)
# print(top_10)

plt.xticks(rotation=45)
dgr = sns.barplot(data=top_10, x='judge', y='cases', hue='cases')
plt.savefig('diagram/judges.png', dpi=300, bbox_inches='tight')