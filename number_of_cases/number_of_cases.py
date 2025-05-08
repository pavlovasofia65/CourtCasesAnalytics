import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('csvs/docs.csv', delimiter="\t")

months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
cases_by_months = []
for m in months:
    cases = get_info_by_month(df, '2024', m)
    cases_by_months.append({'month':m, 'cases': len(cases)})

cases_df = pd.DataFrame(cases_by_months)
dgr = sns.barplot(data=cases_df, x='month', y='cases', hue='cases')
plt.title('Кількість справ за місяцями (2024 рік)')
plt.savefig(f'number_of_cases/number_of_cases.png', dpi=300, bbox_inches='tight')