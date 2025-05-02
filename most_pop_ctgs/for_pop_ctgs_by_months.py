import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import *

# ctgs' codes
df = pd.read_csv('csvs/docs.csv', delimiter="\t")
data = pd.read_json('responses/cases_by_categories.json')
top = data.nlargest(10, 'cases')
ctgs = top['category_code']

def diagram(df, ctg, i):
    data = df[df['category_code'] == ctg]
    months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    info = []
    for m in months:
        cases = len(get_info_by_month(data, '2024', m))
        info.append({'month': m, 'cases': cases})
    df1 = pd.DataFrame(info)

    dgr = sns.barplot(data=df1, x='month', y='cases', hue='cases')
    plt.title(f'{ctgs.iloc[i]}')
    plt.savefig(f'most_pop_ctgs/ctg_diagrams/0{i}-{ctgs.iloc[i]}.png', dpi=300, bbox_inches='tight')


# diagram(df, ctgs.iloc[1], 1)
# diagram(df, ctgs.iloc[3], 3)
# diagram(df, ctgs.iloc[4], 4)
# diagram(df, ctgs.iloc[5], 5)
# diagram(df, ctgs.iloc[6], 6)
# diagram(df, ctgs.iloc[7], 7)
# diagram(df, ctgs.iloc[8], 8)
# diagram(df, ctgs.iloc[9], 9)