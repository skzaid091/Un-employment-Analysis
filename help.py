import pandas as pd

drop_down_months = ['Overall', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']


def str_to_int(obj):
    i = int(obj)
    return i


def temporary(df):
    avg_unrate = df['unrate'].mean()
    avg_unrate_men = df['unrate_men'].mean()
    avg_unrate_women = df['unrate_women'].mean()

    return avg_unrate, avg_unrate_men, avg_unrate_women


def change(obj):
    for i in drop_down_months:
        if obj == drop_down_months.index(i):
            obj = i
    return obj


def result(df, df1, year, month):
    flag = 0
    data = df
    data['month'] = data['month'].apply(change)
    new_data = df1
    if (year == 'Overall') and (month == 'Overall'):
        flag = 1
        temp_df = new_data
    if (year != 'Overall') and (month == 'Overall'):
        flag = 0
        temp_df = data[data['year'] == year]
    if (year == 'Overall') and (month != 'Overall'):
        flag = 0
        temp_df = data[data['month'] == month]
    if (year != 'Overall') and (month != 'Overall'):
        flag = 0
        temp_df = data[(data['year'] == year) & (data['month'] == month)]

    return temp_df, flag


def graph(df, df1, year):
    if year == 'Overall':
        temp = df1['avg_unrate']
    return temp