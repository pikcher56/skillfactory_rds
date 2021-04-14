import pandas as pd

pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 80)


data = pd.read_csv('main_task.csv')
data.columns = ['Restaurant_id', 'City', 'Cuisine_Style', 'Ranking', 'Rating', 'Price_Range', 'Number_Reviews', 'Reviews', 'URL_TA', 'ID_TA']
data.info()

# print(data.Price_Range.unique())
#
# print(len(data[data['Price_Range'] == "$$ - $$$"]))

# print(len(data['City'].unique()))


# print(data[:1].columns)

# for column in data[:1].columns:
#     print(column)
#     print(data[:1][column][0])
#     print(type(data[:1][column][0]))

# r_data = pd.read_csv('reviews.csv', delimiter=";", header=None)
# r_data.columns = ['Restaraunt_id', 'ID_TA', 's1', 's2', 's3', 's4', 's5', 'price', 'city_rating', 'reviews', 'cuisines']
# r_data.columns = ['Restaurant_id', 'City', 'Cuisine Style', 'Ranking', 'Rating', 'Price Range', 'Number of Reviews', 'Reviews', 'URL_TA', 'ID_TA']
# r_data.info()


# d = data[:5]
#
# merged = d.merge(r_data, on="ID_TA", how="left")
# print(merged)

# diff function
# def show_unique_values(dataframe):
#   df = pd.DataFrame(index = dataframe.columns)
#   unique_values_list_for_each_column = [dataframe[col].unique() for col in dataframe.columns]
#   df['Unique values count'] = [len(arr) for arr in unique_values_list_for_each_column]
#   for i in range(20):
#     df[f'Unique value {i}'] = [(arr[i] if i < len(arr) else '') for arr in unique_values_list_for_each_column] #next_display_column
#   with pd.option_context('display.max_colwidth', 25):
#     display(df)


#
# from geopy.distance import geodesic
#
# point_1 = (59.33258, 18.0649)
# point_2 = (59.296162, 18.053225)
# print(geodesic(point_1, point_2).miles)
#
# point_1 = (59.33258, 18.0649)
# point_2 = (59.318535, 18.058828)
# print(geodesic(point_1, point_2).miles)

# print(data['City'].value_counts())

# st = data[data['City'] == 'Stockholm']
# print(st)

#
# data.info()
#
#
# print(data.head())

# vals = set()
# for value in data['Price Range'].values:
#     vals.add(value)
# print(vals)
#
# print(len(data[data['Price Range'] == "$$ - $$$"]))

# cities = set()
# for city in data['City']:
#     cities.add(city)
# print(len(cities))

# cuisines = data['Cuisine Style'].dropna()

# import ast
#
#
# def transform_to_list(data_string):
#     result = ast.literal_eval(data_string)
#     return result
#
#
# cuisines = data['Cuisine Style'].fillna("['Other']")
# cuisines = cuisines.apply(transform_to_list)
# # print(cuisines)
#
# cuisine_all_count = []
# cuisines_all = dict()
# for c_list in cuisines:
#     cuisine_all_count.append(len(c_list))
#     for cuisine in c_list:
#         try:
#             cuisines_all[cuisine] += 1
#         except:
#             cuisines_all[cuisine] = 1
#

# print(len(cuisines_all))
# # print(cuisines_all)
# max = 0
# max_key = ''
# for key, value in cuisines_all.items():
#     if value > max:
#         max = value
#         max_key = key
#
# print(max)
# print(max_key)
#
# print(cuisine_all_count)
# print(sum(cuisine_all_count)/len(cuisine_all_count))


#
#
# Dicts

population = {
    'London': 8908081,
    'Paris' : 2148327,
    'Madrid': 3223334,
    'Barcelona': 1620343,
    'Berlin': 3769495,
    'Milan': 1378689,
    'Rome': 2870500,
    'Prague': 1324277,
    'Lisbon': 505526,
    'Vienna': 1897491,
    'Amsterdam': 857713,
    'Brussels': 179277,
    'Hamburg': 1899160,
    'Munich': 1471508,
    'Lyon': 513275,
    'Stockholm': 975904,
    'Budapest': 1752286,
    'Warsaw': 1790658,
    'Dublin': 554554,
    'Copenhagen': 794128,
    'Athens': 664046,
    'Edinburgh': 488100,
    'Zurich': 415215,
    'Oporto': 214349,
    'Geneva': 201818,
    'Krakow': 769498,
    'Oslo': 681067,
    'Helsinki': 650058,
    'Bratislava': 437725,
    'Luxembourg': 613894,
    'Ljubljana': 284355
}


is_capital = {
    'London': 1,
    'Paris' : 1,
    'Madrid': 1,
    'Barcelona': 0,
    'Berlin': 1,
    'Milan': 0,
    'Rome': 1,
    'Prague': 1,
    'Lisbon': 1,
    'Vienna': 1,
    'Amsterdam': 1,
    'Brussels': 1,
    'Hamburg': 0,
    'Munich': 0,
    'Lyon': 0,
    'Stockholm': 1,
    'Budapest': 1,
    'Warsaw': 1,
    'Dublin': 1,
    'Copenhagen': 1,
    'Athens': 1,
    'Edinburgh': 1,
    'Zurich': 1,
    'Oporto': 0,
    'Geneva': 1,
    'Krakow': 0,
    'Oslo': 1,
    'Helsinki': 1,
    'Bratislava': 1,
    'Luxembourg': 1,
    'Ljubljana': 1
}


countries_dict = {
    'London': 'England',
    'Paris': 'France',
    'Madrid': 'Spain',
    'Barcelona': 'Spain',
    'Berlin': 'Germany',
    'Milan': 'Italy',
    'Rome': 'Italy',
    'Prague': 'Czech',
    'Lisbon': 'Portugal',
    'Vienna': 'Austria',
    'Amsterdam': 'Holland',
    'Brussels': 'Belgium',
    'Hamburg': 'Germany',
    'Munich': 'Germany',
    'Lyon': 'France',
    'Stockholm': 'Sweden',
    'Budapest': 'Romania',
    'Warsaw': 'Poland',
    'Dublin': 'Ireland',
    'Copenhagen': 'Denmark',
    'Athens': 'Greece',
    'Edinburgh': 'Scotland',
    'Zurich': 'Switzerland',
    'Oporto': 'Portugal',
    'Geneva': 'Switzerland',
    'Krakow': 'Poland',
    'Oslo': 'Norway',
    'Helsinki': 'Finland',
    'Bratislava': 'Slovakia',
    'Luxembourg': 'Luxembourg',
    'Ljubljana': 'Slovenia'
}

# print(data['City'].value_counts())




