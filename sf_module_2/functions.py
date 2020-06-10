from IPython.display import display
import matplotlib.pyplot as plt
from itertools import combinations
from scipy.stats import ttest_ind
import seaborn as sns
import pandas as pd
import random


# sns.set(style="darkgrid")


def show_frame_info(df):
    """
    Show detailed info of DataFrame
    :param df: DataFrame
    :return: void
    """
    # display(df.info())
    display(df.head())
    print("Dataset info")
    display(df.info())

    print(f"Rows amount in dataset - {df.shape[0]}")
    print(f"Columns amount in dataset - {df.shape[1]}")
    print()
    print("Ho many passes(Empty values) in dataset")
    print(df.isnull().sum())


def show_column_info(df, column, show_value_counts=True, bins=10):
    """
    Show detailed info of column in DataFrame
    :param bins: Parameter for method df[column].hist()
    :param show_value_counts: Show or not value_counts table
    :param df: DataFrame
    :param column: column from DataFrame
    :return:
    """
    column_types = {
        'type1': ['object'],
        'type2': ['int64', 'float64']
    }
    if column in df.columns:
        print(f"INFO FOR COLUMN: {column}")
        print()
        column_type = df[column].dtype
        print(f"Column type: {column_type}")
        display(df[column].describe())
        # print(f"Unique values count: {df[column].nunique()}")
        # print(f"Not empty values count: {df[column].count()}")
        print(f"Passes (NAN or Empty values): {df[column].isnull().sum()}")
        print()
        if show_value_counts:
            display(pd.DataFrame(df[column].value_counts(dropna=False)))

        if column_type in column_types['type1']:
            sns.countplot(y=column, data=df)
        elif column_type in column_types['type2']:
            df[column].hist(bins=bins)
        else:
            print(f"Unknown column type {column_type} for column {column}!")
    else:
        print(f"Column {column} not found in DataFrame!")


def show_box_plot(df, column, second_column='score', size_x=14, size_y=4):
    """
    Show boxplot
    :param size_y: figure y size
    :param size_x: figure x size
    :param df: DataFrame
    :param column: column for x data
    :param second_column: column for y data
    :return: void
    """
    fig, ax = plt.subplots(figsize=(size_x, size_y))
    sns.boxplot(x=column, y=second_column,
                data=df.loc[df.loc[:, column].isin(df.loc[:, column].value_counts().index[:])],
                ax=ax)
    plt.xticks(rotation=45)
    ax.set_title('Boxplot for ' + column)
    plt.show()


def show_iqr_histogram(df, column):
    """
    Show outliers
    :param df: DataFrame
    :param column: column from DataFrame
    :return:
    """
    median = df[column].median()
    iqr = df[column].quantile(0.75) - df[column].quantile(0.25)
    perc25 = df[column].quantile(0.25)
    perc75 = df[column].quantile(0.75)
    print('25 percentile: {},'.format(perc25), '75 percentile: {},'.format(perc75)
          , "IQR: {}, ".format(iqr), "Outliers bound: [{f}, {l}].".format(f=perc25 - 1.5 * iqr, l=perc75 + 1.5 * iqr))
    df[column].loc[df[column].between(perc25 - 1.5 * iqr, perc75 + 1.5 * iqr)].hist(bins=10, range=(0, 20),
                                                                                      label='IQR')
    plt.legend()


def get_stat_dif(df, column):
    """
    Student test
    :param df:
    :param column:
    :return:
    """
    cols = df.loc[:, column].value_counts().index
    combinations_all = list(combinations(cols, 2))
    for comb in combinations_all:
        if ttest_ind(df.loc[df.loc[:, column] == comb[0], 'score'],
                     df.loc[df.loc[:, column] == comb[1], 'score']).pvalue \
                <= 0.05/len(combinations_all):  # took into account Bonferoni amendment
            print('Found statistical significant difference for column ', column)
            break


def convert_to_value(value):
    """
    Change str values to int
    :param value:
    :return:
    """
    if pd.isnull(value):
        return value
    if value == 'LE3':
        return 1
    if value == 'GT3':
        return 2
    if value == 'T':
        return 1
    if value == 'A':
        return 2
    if value == 'yes':
        return 1
    if value == 'no':
        return 0
    if value == 'M':
        return 1
    if value == 'F':
        return 0


address_values = ['U', 'R']


def fill_address(df, address, traveltime):
    """
    Fill Nan values for column address
    :param df:
    :param address:
    :param traveltime:
    :return:
    """
    return_value = None
    if address not in address_values:
        traveltime_num = float(traveltime)
        if traveltime_num <= 2:
            return_value = 'U'
        elif traveltime_num > 2:
            return_value = 'R'
        else:
            return_value = df['address'].mode()[0]
    else:
        return_value = address
    return return_value


famsize_values = ["GT3", "LE3"]


def fill_famsize(df, famsize, Pstatus):
    return_value = None
    # print(famsize)
    if famsize not in famsize_values:
        if Pstatus == 'T':
            return_value = 'GT3'
        elif Pstatus == 'A':
            return_value = 'LE3'
        else:
            return_value = df['famsize'].mode()[0]
    else:
        return_value = famsize
    return return_value


pstatus_values = ['A', 'T']


def fill_pstatus(row):
    """
    Fill NaN values ftor column pstatus
    :param row:
    :return:
    """
    return_value = None
    if row['Pstatus'] not in pstatus_values:
        if row['famsize'] == 'GT3':
            return_value = 'T'
        elif row['famsize'] == 'LE3':
            return_value = 'A'
        else:
            return_value = row['Pstatus']
    else:
        return_value = row['Pstatus']
    return return_value


fedu_values = [1.0, 2.0, 3.0, 4.0]


def fill_fedu(row):
    """
    Fill NaN values for column Fedu
    :param df:
    :param index:
    :return:
    """
    return_value = None
    if row['Fedu'] not in fedu_values:
        if row['Fjob'] == 'teacher':
            return_value = 4.0
        else:
            if row['Medu'] == 4.0:
                return_value = 3.0
            else:
                return_value = row['Medu']
    else:
        return_value = row['Fedu']
    return return_value


traveltime_values = [1.0, 2.0, 3.0, 4.0]


def fill_traveltime(row):
    """
    Fill NaN values for column traveltime
    :param row:
    :return:
    """
    return_value = None
    if row['traveltime'] not in traveltime_values:
        if row['address'] == 'U':
            if row['reason'] == 'home':
                return_value = 1.0
            else:
                return_value = 2.0
        elif row['address'] == 'R':
            if row['reason'] == 'home':
                return_value = 3.0
            else:
                return_value = 4.0
    else:
        return_value = row['traveltime']
    return return_value







