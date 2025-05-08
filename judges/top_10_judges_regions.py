import pandas as pd
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from functions import *

df = pd.read_csv('docs.csv')
judges = pd.read_csv('top_10_judges.csv')
judges_courts = []

# for judge in judges['judge']:
#     info = get_judge_cases(df, judge)
#     courts = info.groupby()['doc_id'].count()

info = get_judge_cases(df, judges[0])
print(info)