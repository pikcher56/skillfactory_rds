import pandas as pd
from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations
from scipy.stats import ttest_ind
import math

from functions import show_frame_info, show_column_info, show_box_plot, convert_to_value, get_stat_dif, fill_address

# show more rows
pd.set_option('display.max_rows', 200)
# show more columns
pd.set_option('display.max_columns', 80)


df = pd.read_csv('stud_math.csv')
df['counter'] = 1
# display(df['address'].mode())
# df['address'].fillna(1, inplace=True)
# show_column_info(df, 'address')
# display(df.info())
# show_frame_info(df)


show_column_info(df, 'address')
# df.loc[df['address'].isnull() & (df['traveltime'] == 1.0), 'address'].fillna('U', inplace=True)
# df['adr'] = df.apply(lambda x: 'U' if x['address'] == 'NaN' and x.traveltime == 1 else 'R', axis=1)
df['address'] = df.apply(lambda x: fill_address(x['address'], x['traveltime']), axis=1)
show_column_info(df, 'address')



# df['famsize'] = df['famsize'].apply(convert_to_value)
# df['Pstatus'] = df['Pstatus'].apply(convert_to_value)

# sns.jointplot(x='famsize', y='Pstatus', data=df)


# df.plot(x='famsize',
#         y='Pstatus',
#         kind='scatter',
#         grid=True,
#         title="m1")

# df.groupby(['famsize', 'Pstatus']).hist()
# show_column_info(df, 'school')
#
# show_column_info(df, 'age')
#
# show_column_info(df, 'score')

# show_column_info(df, 'traveltime')

# rm1 = df[(df['sex'] == 'F') & (df['romantic'] == 'yes')]
# # display(rm1)
# show_box_plot(rm1, 'age')
#
# rm2 = df[(df['sex'] == 'F') & (df['romantic'] == 'no')]
# show_box_plot(rm2, 'age')


# table = pd.pivot_table(df, columns=['Pstatus'], index=['famsize'], aggfunc={'Pstatus':sum})
# display(table)
#
# data = df[df['famsize'].isnull() & df['Pstatus'].isnull()]
# display(data)
#
# tr_data = df[df['traveltime'].isnull()]
# display(tr_data)

# display(df.groupby(['address', 'school', 'age']).traveltime.mean())
# df.groupby(['school', 'age']).traveltime.mean().hist()
# df.groupby(['address', 'school']).traveltime.mean().hist()
# df.groupby(['address', 'school', 'age']).traveltime.mean().hist()

# sns.pairplot(df, kind='reg')


# show_box_plot(df, 'school', 'age')

# df['Par_edu2'] = df.apply(lambda x: x.Medu if x.guardian == 'mother'
#                 else (x.Fedu if x.guardian == 'father' else x[['Medu','Fedu']].max()), axis=1)
# display(df)

# fs_df = df.pivot_table(values='counter', index=['famsize'], columns='Pstatus', aggfunc='count', fill_value=0)
# display(fs_df)

# change value
# df.loc[df['Fedu'] == 40, 'Fedu'] = 1
# df.Fedu.hist()

# df['edu_avg'] = df.apply(lambda x: x[['Medu', 'Fedu']].mean(), axis=1)

# for column in (col for col in df.columns if df[col].dtype == 'object'):


import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)


# df.loc[df['Fedu'] == 40, 'Fedu'] = 4
# df['Medu'] = df['Medu'].fillna(df['Medu'].median(), inplace=True)
# df['Fedu'] = df['Fedu'].fillna(df['Fedu'].median(), inplace=True)

# df = df.apply(convert_to_value)


# for column in (col for col in df.columns if df[col].dtype == 'object'):
#     df[column] = df[column].apply(convert_to_value)
#
# display(df)


# for column in ['Mjob', 'Fjob', 'Medu', 'Fedu', 'famrel', 'freetime', 'goout', 'health']:
# for column in (col for col in df.columns if df[col].dtype == 'object'):
#     get_stat_dif(df, column)





# def custom_func(value1, value2):
#     # print(value1)
#     # print(value2)
#     return 1
#
#
# df['b_edu'] = df.apply(lambda x: custom_func(x['Medu'], x['Fedu']), axis=1)






# plt.show()



