import numpy as np
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

import matplotlib.dates as mdates

import folium


case = pd.read_csv('data/datasets_527325_1157664_Case.csv')
patient = pd.read_csv('data/datasets_527325_1157664_PatientInfo.csv')
patientRoute = pd.read_csv('data/datasets_527325_1157664_PatientRoute.csv')
policy = pd.read_csv('data/datasets_527325_1157664_Policy.csv')
region = pd.read_csv('data/datasets_527325_1157664_Region.csv')
search = pd.read_csv('data/datasets_527325_1157664_SearchTrend.csv')
time = pd.read_csv('data/datasets_527325_1157664_Time.csv')
age = pd.read_csv('data/datasets_527325_1157664_TimeAge.csv')
gender = pd.read_csv('data/datasets_527325_1157664_TimeGender.csv')
province = pd.read_csv('data/datasets_527325_1157664_TimeProvince.csv')
# seoul = pd.read_csv('SeoulFloating.csv')
# weather = pd.read_csv('Weather.csv')

# print(age.info())
# print(gender.info())
# print(province.info())
# print(age.isnull().sum())
# print(gender.isnull().sum())
# print(province.isnull().sum())

print(age.head())
print(age.tail())
print(gender.head())
print(province.head())

# fig, ax = plt.subplots(figsize=(20,24))
# bar = ax.bar(age['age'], age['confirmed'])

# 連續圖
# for title in age['age']:
#     ax.plot(age.date.unique(), age.loc[age['age'] == title, 'confirmed'], color = 'blue', linewidth = 2)

# pie plot
# order = pd.DataFrame()
# order['age'] = age['age'].unique()
# size = list(age.loc[age['date'] == '2020-05-14', 'confirmed'])
# order['size'] = size
# order = order.sort_values(by=['size'])

# ax.pie(order['size'], labels=order['age'], autopct='%.2f%%')
# plt.axis('equal')

# pie plot
# fig, ax = plt.subplots(figsize=(20,24))
# order = pd.DataFrame()
# order['age'] = age['age'].unique()
# size = list(age.loc[age['date'] == '2020-05-14', 'deceased'])
# order['size'] = size
# order = order.sort_values(by=['size'])

# ax.pie(order['size'], labels=order['age'], autopct='%.2f%%')
# plt.axis('equal')

# daily confirmed
for title in age['age'].unique():
    day = age.loc[age['age']==title, 'confirmed']
    age.loc[age['age']==title, 'daily_confirmed'] = day.shift(-1) - day

age.groupby(['date','age'])['daily_confirmed'].sum() .unstack('age', fill_value=0).plot(legend=True, figsize=(20,24))

# daily deceased
for title in age['age'].unique():
    day = age.loc[age['age']==title, 'deceased']
    age.loc[age['age']==title, 'daily_deceased'] = day.shift(-1) - day

age.groupby(['date','age'])['daily_deceased'].sum() .unstack('age', fill_value=0).plot(legend=True, figsize=(20,24))



# plt.figure()
# fig, ax = plt.subplots(figsize=(20,24))
# sex_bar = ax.bar(gender['sex'], gender['confirmed'])

# pie plot
# order = pd.DataFrame()
# order['sex'] = gender['sex'].unique()
# size = list(gender.loc[gender['date'] == '2020-05-14', 'confirmed'])
# order['size'] = size
# order = order.sort_values(by=['size'])
# fig, ax = plt.subplots(figsize=(20,24))
# ax.pie(order['size'], labels=order['sex'], autopct='%.2f%%')
# plt.axis('equal')


# 轉換日期時間，繪製chart用
# gender.index = pd.to_datetime(gender['date'])
# 將時間日期轉換成Matplotlib date format
# pdates = mdates.date2num(gender.loc[gender['sex'] == 'male', 'index'])

# 連續圖
# ax.plot(gender.index.unique(), gender.loc[gender['sex'] == 'male', 'confirmed'], color = 'blue', linewidth = 2)
# ax.plot(gender.index.unique(), gender.loc[gender['sex'] == 'female', 'confirmed'], color = 'red', linewidth = 2)

# daily confirmed
for title in gender['sex'].unique():
    day = gender.loc[gender['sex']==title, 'confirmed']
    gender.loc[gender['sex']==title, 'daily_confirmed'] = day.shift(-1) - day

gender.groupby(['date','sex'])['daily_confirmed'].sum() .unstack('sex', fill_value=0).plot(legend=True, figsize=(20,24))

# daily deceased
for title in gender['sex'].unique():
    day = gender.loc[gender['sex']==title, 'deceased']
    gender.loc[gender['sex']==title, 'daily_deceased'] = day.shift(-1) - day

gender.groupby(['date','sex'])['daily_deceased'].sum() .unstack('sex', fill_value=0).plot(legend=True, figsize=(20,24))


# plt.figure()
# fig, ax = plt.subplots(figsize=(20,24))
# province_bar = ax.bar(province['province'], province['confirmed'])

# pie plot
# order = pd.DataFrame()
# order['province'] = province['province'].unique()
# size = list(province.loc[province['date'] == '2020-05-14', 'confirmed'])
# order['size'] = size
# order = order.sort_values(by=['size'])

# fig, ax = plt.subplots(figsize=(20,24))
# ax.pie(order['size'], labels=order['province'], autopct='%.2f%%')
# plt.axis('equal')


# 連續圖
# for title in province['province']:
#     ax.plot(province.date.unique(), province.loc[province['province'] == title, 'confirmed'], color = 'blue', linewidth = 2)
# ax.plot(province.date.unique(), province.loc[province['province'] == 'Daegu', 'confirmed'], color = 'blue', linewidth = 2)

# Total		
# total_list = province.groupby('date').sum().confirmed
# fig, ax = plt.subplots(figsize=(13, 7))
# plt.title('Cumulative Confirmed Cases (total)', fontsize=17)
# ax.set_xlabel('Date', size=13)
# ax.set_ylabel('Number of cases', size=13)
# plt.plot(province.date.unique()
#          , province.groupby('date').sum().confirmed)
# ax.set_xticks(ax.get_xticks()[::11])

# print(province['time'].unique())

# Daegu
# loc = province.loc[province['province'] == 'Daegu']
# # fig, ax = plt.subplots(figsize=(13, 7))
# plt.title('Cumulative Confirmed Cases (Daegu)', fontsize=17)
# ax.set_xlabel('Date', size=13)
# ax.set_ylabel('Number of cases', size=13)
# plt.plot(province.date.unique(), loc['confirmed'])
# ax.set_xticks(ax.get_xticks()[::11])

# # Daegu
# loc = province.loc[province['province'] == 'Gyeongsangbuk-do']
# # fig, ax = plt.subplots(figsize=(13, 7))
# plt.title('Cumulative Confirmed Cases (Gyeongsangbuk-do)', fontsize=17)
# ax.set_xlabel('Date', size=13)
# ax.set_ylabel('Number of cases', size=13)
# plt.plot(province.date.unique(), loc['confirmed'])
# ax.set_xticks(ax.get_xticks()[::11])

# main
# loc = province[(province.province=='Daegu') | (province.province=='Gyeongsangbuk-do')].groupby('date').sum().confirmed
# print(loc)
# # fig, ax = plt.subplots(figsize=(13, 7))
# plt.title('Cumulative Confirmed Cases (add)', fontsize=17)
# ax.set_xlabel('Date', size=13)
# ax.set_ylabel('Number of cases', size=13)
# plt.plot(province.date.unique(), loc)
# ax.set_xticks(ax.get_xticks()[::11])

# other
# loc = province[(province.province!='Daegu') & (province.province!='Gyeongsangbuk-do')].groupby('date').sum().confirmed
# print(loc)
# # fig, ax = plt.subplots(figsize=(13, 7))
# plt.title('Cumulative Confirmed Cases (add)', fontsize=17)
# ax.set_xlabel('Date', size=13)
# ax.set_ylabel('Number of cases', size=13)
# plt.plot(province.date.unique(), loc)
# ax.set_xticks(ax.get_xticks()[::11])

# daily confirmed
for title in province['province'].unique():
    day = province.loc[province['province']==title, 'confirmed']
    province.loc[province['province']==title, 'daily_confirmed'] = day.shift(-1) - day

province.groupby(['date','province'])['daily_confirmed'].sum() .unstack('province', fill_value=0).plot(legend=True, figsize=(20,24))

# daily deceased
for title in province['province'].unique():
    day = province.loc[province['province']==title, 'deceased']
    province.loc[province['province']==title, 'daily_deceased'] = day.shift(-1) - day

province.groupby(['date','province'])['daily_deceased'].sum() .unstack('province', fill_value=0).plot(legend=True, figsize=(20,24))

# daily released
for title in province['province'].unique():
    day = province.loc[province['province']==title, 'released']
    province.loc[province['province']==title, 'daily_released'] = day.shift(-1) - day

province.groupby(['date','province'])['daily_released'].sum() .unstack('province', fill_value=0).plot(legend=True, figsize=(20,24))

plt.show()


# 連續 圓餅 柱狀

