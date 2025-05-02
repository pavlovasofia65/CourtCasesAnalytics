import json
import pandas as pd
import os

# 0. Функція для зберігання результатів у файли
def save_to_file(data, name):
    folder = 'responses'
    os.makedirs(folder, exist_ok = True)
    path = os.path.join(folder, name)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


#  1. Функція для пошуку судовго рішення за id
def get_by_id(df, doc_id):
    if doc_id:
        info = df[(df['doc_id']==doc_id)]
        info_list = info.to_dict(orient='records')
        save_to_file(info_list, 'doc_id.json')
        return info_list
    else:
        return "There is an error"

# 2. К-ть судових рішень за кодом суду
def get_info_by_court(df, court_code):
    courts_info = df.groupby('court_code')['doc_id'].count().to_dict()
    save_to_file(courts_info, 'courts_info.json')
    return courts_info

# 3. Пошук судових рішень судді
def get_judge_cases(df, judge):
    if judge:
        info = df[(df['judge'].str.contains(judge, na = False))]
        info_judge = info.to_dict(orient='records')
        save_to_file(info_judge, 'judge_info.json')
        return info_judge
    else:
        return "There is an error"

# 4. Порахувати к-ть рішень для кожного судді
def cases_by_judge(df):
    count_judges_work = df.groupby('judge')['doc_id'].count().to_dict()
    save_to_file(count_judges_work, 'for_every_judge.json')
    return count_judges_work

# 5. Пошук рішень за певний місяць, рік
def get_info_by_month(df, year, month):
    if month and year:
        info = df[df['adjudication_date'].str.contains(f"{year}-{month}", na=False)]
        # save_to_file(info.to_dict(orient='records'), 'info_by_month.json')
        return info
    else:
        return "There is an error"

# 6. Сортування відповіді
def sort_df(df, col, asc: bool):
    return df.sort_values(by = col, ascending = asc)

# 7. Скільки суддів у кожному суді
def judges_by_courts(df):
    info = df.groupby('court_code')['judge'].unique().apply(list).to_dict()
    save_to_file(info, 'judges_by_courts.json')

# 8. К-ть рішень для кожної категорії
def cases_by_categories(df, category):
    ctg = sort_df(category, 'category_code', True)
    info = df.groupby('category_code')['doc_id'].count().reset_index()
    info = info.rename(columns={'doc_id': 'cases'})
    df1 = info.merge(ctg, on='category_code', how='left')
    save_to_file(df1.to_dict(orient='records'), 'cases_by_categories.json')

# 9. К-ть судів у кожній області
def count_courts_by_regions(courts, regions):
    info = courts.groupby('region_code')['court_code'].count().reset_index()
    df1 = info.merge(regions, on='region_code', how='left')

    df1.insert(1, 'name', df1.pop('name'))
    df1.rename(columns={'court_code': 'number of courts'}, inplace=True)
    save_to_file(df1.to_dict(orient='records'), 'number_of_courts_by_regions.json')
    return df1

# 10. Суди у якійсь області
def get_courts_by_region(courts, region):
    df1 = courts[courts['region_code'] == region]
    df1.index = df1.reset_index(drop=True)
    save_to_file(df1.to_dict(orient='records'), 'court_of_region.json')
    return df1

# 11. К-ть рішень судді за якийсь місяць якогось року
def judge_cases_by_month(df, judge, month, year):
    df_judge = pd.DataFrame(get_judge_cases(df, judge))
    df_judge['adjudication_date'] = df_judge['adjudication_date'].astype(str)
    df_cases = df_judge[df_judge['adjudication_date'].str.contains(f"{year}-{month}", na=False)]
    # save_to_file(df_cases.to_dict(orient='records'), 'judge_cases_by_month.json')
    return len(df_cases)

# 12. Рішення за якоюсь категорією
def cases_category(df, ctgs: list):
    all_info = []
    for ctg in ctgs:
        cases = df[df['category_code'] == ctg]
        dates = cases['adjudication_date']
        years = sorted(list(set([date[:4] for date in dates])))
        cases_in_years = []
        for year in years:
            info = cases[cases['adjudication_date'].str.contains(f"{year}", na=False)]
            cases_in_years.append({
                'year': year,
                'cases': len(info)})
        all_info.append(pd.DataFrame(cases_in_years))
    return all_info

