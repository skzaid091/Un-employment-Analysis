import pandas as pd
import streamlit as st
import help
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout='wide')
data = pd.read_csv('unemployment_rate_data.csv')


def empty_space():
    col4, col5, col6 = st.columns(3)
    with col4:
        st.write('')
        st.write('')
        st.write('')
    with col5:
        pass
    with col6:
        pass


data[['month', 'day', 'year']] = data['date'].str.split('/', expand=True)

data.drop('day', axis=1, inplace=True)
data.drop('date', axis=1, inplace=True)

temp1 = data.pop('year')
temp2 = data.pop('month')

data.insert(0, 'year', temp1)
data.insert(1, 'month', temp2)

data['month'] = data['month'].apply(help.str_to_int)
data['year'] = data['year'].apply(help.str_to_int)

years = data['year'].unique()

new_data = pd.DataFrame()
lst1 = []
lst2 = []
lst3 = []
lst4 = []
for i in years:
    df = data[data['year'] == i]
    temp = help.temporary(df)
    lst1.append(i)
    lst2.append(temp[0])
    lst3.append(temp[1])
    lst4.append(temp[2])

new_data[['year', 'avg_unrate', 'avg_unrate_men', 'avg_unrate_women']] = pd.DataFrame([lst1, lst2, lst3, lst4]).T
new_data['year'] = new_data['year'].apply(lambda x: int(x))

st.sidebar.title('US Un-Employment Analysis (1948 - 2021)')

st.sidebar.title('        ')

drop_down_years = years.tolist()
drop_down_years.insert(0, 'Overall')
year = st.sidebar.selectbox('Select Year', drop_down_years)

drop_down_months = ['Overall', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
month = st.sidebar.selectbox('Select Month', drop_down_months)


col1, col2, col3 = st.columns(3)
with col1:
    st.header('First Year')
    st.subheader(years[0])
with col2:
    st.header('Last Year')
    st.subheader(years[-1])
with col3:
    st.header('Total Years')
    st.subheader(len(years))

empty_space()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.header('Highest Rate')
    st.subheader(str(max(new_data['avg_unrate']))[0:6])
with col2:
    st.header('Year')
    st.subheader(str(new_data[new_data['avg_unrate'] == max(new_data['avg_unrate'])]['year'].iloc[0]))
with col3:
    st.header('Lowest Rate')
    st.subheader(str(min(new_data['avg_unrate']))[0:6])
with col4:
    st.header('Year')
    st.subheader(str(new_data[new_data['avg_unrate'] == min(new_data['avg_unrate'])]['year'].iloc[0]))

empty_space()

st.header('Overall Highest Un-employment Rate')
st.subheader('Men : ' + str(max(new_data['avg_unrate_men'])))
st.subheader('Women : ' + str(max(new_data['avg_unrate_women'])))
empty_space()

st.header('Un_employment Rate Tally')
var, flag = help.result(data, new_data, year, month)
if flag == 1:
    st.table(var)
else:
    st.table(var.iloc[0:, [0, 1, 2, 3, 4, 5]])

empty_space()

if year == 'Overall':
    fig, fx = plt.subplots()
    fx = sns.lineplot(data=new_data, x='year', y='avg_unrate')
    plt.figure(figsize=(15, 15))
    st.title('Un-employment over the Years')
    st.pyplot(fig)
if year != 'Overall':
    fig, fx = plt.subplots()
    fx = sns.lineplot(data=data[data['year'] == year], x='month', y='unrate')
    plt.figure(figsize=(15, 15))
    st.title('Un-employment in year : ' + str(year))
    st.pyplot(fig)

