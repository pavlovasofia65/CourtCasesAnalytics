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

dgr = sns.barplot(data=top, x='category_code', y='cases', hue='cases')
plt.title('Найпопулярніші категорії справ')
plt.savefig(f'most_pop_ctgs/categories.png', dpi=300, bbox_inches='tight')