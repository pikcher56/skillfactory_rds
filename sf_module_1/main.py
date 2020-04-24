from IPython.display import display
import pandas as pd
import collections
from itertools import combinations
import numpy as np

data = pd.read_csv('data.csv')

# answers list
answer_ls = []

films = data
# 1
print(films[films['budget'] == films['budget'].max()]['imdb_id'])
print(films['imdb_id'][films['budget'].idxmax()])
answer_ls.append("4 - The Warrior's Way (tt1032751)")

# 2
print(films['imdb_id'][films['runtime'].idxmax()])
answer_ls.append("2 - Gods and Generals (tt0279111)")

# 3
print(films['imdb_id'][films['runtime'].idxmin()])
answer_ls.append("3 - Winnie the Pooh tt1449283")

# # 4
# print(data['runtime'].mean())
answer_ls.append("2 - 110")

# 5
print(data['runtime'].median())
answer_ls.append("1 - 106")

# 6
data['profit_value'] = data['revenue'] - data['budget']
print(data['imdb_id'][data['profit_value'].idxmax()])
answer_ls.append("5 - Avatar tt0499549")

# 7
data['profit_value'] = data['revenue'] - data['budget']
print(data['imdb_id'][data['profit_value'].idxmin()])
answer_ls.append("2 - The Warrior's Way tt1032751")

# 8
films = data[data['revenue'] > data['budget']]
print(len(films))
answer_ls.append("1 - 1478")

# 9
films = data.query('release_year == 2008')
print(films['imdb_id'][films['popularity'].idxmax()])
answer_ls.append("4 - The Dark Knight tt0468569")

# 10
data['profit_value'] = data['revenue'] - data['budget']
films = data.query('release_year == ["2012", "2013", "2014"]')
print(films['imdb_id'][films['profit_value'].idxmin()])
answer_ls.append("5 - The Lone Ranger tt1210819")

# 11
genres_all = data['genres'].str.split('|').sum()
genres = pd.DataFrame(genres_all)
print(genres[0].value_counts().head(1))
answer_ls.append("3 - Drama")

# 12
data['profit_value'] = data['revenue'] - data['budget']
films = data[data['profit_value'] > 0]
genres_all = films['genres'].str.split('|').sum()
genres_counter = collections.Counter(genres_all)
print(genres_counter.most_common(1))
answer_ls.append("3 - Drama")

# 13
directors = data['director'].str.split('|').sum()
directors_unique = collections.Counter(directors)
print(directors_unique.most_common(1))
answer_ls.append("3 - Steven Soderbergh")

# 14
data['profit_value'] = data['revenue'] - data['budget']
films = data[data['profit_value'] > 0]
directors_all = films['director'].str.split('|').sum()
directors = pd.DataFrame(directors_all)
print(directors[0].value_counts().head(1))
answer_ls.append("2 - Ridley Scott ")

# 15
data['profit_value'] = data['revenue'] - data['budget']
grouped_data = data.groupby('director')['profit_value'].sum()
print(grouped_data.sort_values(ascending=False))
answer_ls.append("5 - Peter Jackson")

# 16
data['profit_value'] = data['revenue'] - data['budget']
counter = collections.Counter()
for film_index in range(len(data)):
    profit_value = data.loc[film_index]['profit_value']
    actors = data.loc[film_index]['cast']
    for actor in actors.split('|'):
        counter[actor] += profit_value
print(counter.most_common(1))
answer_ls.append("1 - Emma Watson")

# 17
data['profit_value'] = data['revenue'] - data['budget']
films = data[data['release_year'] == 2012]
counter = collections.Counter()
for film_id in films['imdb_id']:
    profit_value = films[films['imdb_id'] == film_id]['profit_value'].iloc[0]
    actors = films[films['imdb_id'] == film_id]['cast'].iloc[0]
    for actor in actors.split('|'):
        counter[actor] += profit_value
print(counter.most_common()[-1:])
answer_ls.append("3 - Kirsten Dunst")

# 18
films = data[data['budget'] > data['budget'].mean()]
actors_all = films['cast'].str.split('|').sum()
actors = pd.DataFrame(actors_all)
print(actors[0].value_counts().head(1))
answer_ls.append("3 - Matt Damon")

# 19
films = data[data['cast'].str.contains('Nicolas Cage')]
genres_all = films['genres'].str.split('|').sum()
genres = pd.DataFrame(genres_all)
print(genres[0].value_counts().head(1))
answer_ls.append("2 - Action")

# 20
companies_all = data['production_companies'].str.split('|').sum()
companies = pd.DataFrame(companies_all)
print(companies[0].value_counts().head(1))
answer_ls.append("1 - Universal Pictures (Universal)")

# 21
films = data[data['release_year'] == 2015]
companies_all = films['production_companies'].str.split('|').sum()
companies = pd.DataFrame(companies_all)
print(companies[0].value_counts().head(1))
answer_ls.append("4 - Warner Bros")

# 22
data['profit_value'] = data['revenue'] - data['budget']
data = data[data['genres'].str.contains("Comedy")]
counter = collections.Counter()
for film_id in data['imdb_id']:
    profit_value = data[data['imdb_id'] == film_id]['profit_value'].iloc[0]
    companies = data[data['imdb_id'] == film_id]['production_companies'].iloc[0]
    for company in companies.split('|'):
        counter[company] += profit_value
print(counter.most_common(1))
answer_ls.append("2 - Universal Pictures (Universal)")

# 23
data['profit_value'] = data['revenue'] - data['budget']
data = data[data['release_year'] == 2012]
counter = collections.Counter()
for film_id in data['imdb_id']:
    profit_value = data[data['imdb_id'] == film_id]['profit_value'].iloc[0]
    companies = data[data['imdb_id'] == film_id]['production_companies'].iloc[0]
    for company in companies.split('|'):
        counter[company] += profit_value
print(counter.most_common(1))
answer_ls.append("3 - Columbia Pictures")

# 24
data['profit_value'] = data['revenue'] - data['budget']
films = data[data['production_companies'].str.contains('Paramount Pictures')]
print(films.sort_values(by=['profit_value']).head(1))
answer_ls.append("1 - K-19: The Widowmaker tt0267626")

# 25
data['profit_value'] = data['revenue'] - data['budget']
grouped_data = data.groupby('release_year')['profit_value'].sum()
print(grouped_data.sort_values(ascending=False))
answer_ls.append("5 - 2015")

# 26
data['profit_value'] = data['revenue'] - data['budget']
films = data[data['production_companies'].str.contains('Warner Bros')]
grouped_data = films.groupby('release_year')['profit_value'].sum()
print(grouped_data.sort_values(ascending=False))
answer_ls.append("1 - 2014")

# 27
data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
print(data['month'].value_counts(ascending=False).head(1))
answer_ls.append("4 - Сентябрь")

# 28
data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
films = data[data['month'].isin(['6', '7', '8'])]
print(len(films))
answer_ls.append("2 - 450")

# 29
data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
films = data[data['month'].isin(['12', '1', '2'])]
directors_all = films['director'].str.split('|').sum()
director_counter = collections.Counter(directors_all)
print(director_counter.most_common(1))
answer_ls.append("5 - Peter Jackson")

# 30
data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
data['year'] = data['release_date'].apply(lambda x: x.split('/')[2])
data['profit_value'] = data['revenue'] - data['budget']
# pivot_data = data.pivot_table(values=['profit_value'],index=['release_year', 'month'],aggfunc='sum').reset_index()
pivot_data = data.pivot_table(values='profit_value',
                              aggfunc='sum',
                              columns='month',
                              index='release_year')
# display(pivot_data)
# print(pivot_data.idxmax(axis=1))
print(pivot_data.idxmax(axis=1).value_counts().head(1))
answer_ls.append("2 - Июнь")

# 31
data['title_length'] = data['original_title'].str.len()
studios_all = data['production_companies'].str.split('|').sum()
studios_unique = np.unique(np.array(studios_all))
word_data = []
for studio in studios_unique:
    mean = data[data['production_companies'].str.contains(studio)]['title_length'].mean()
    word_data.append([studio, mean])
frame = pd.DataFrame(word_data)
print(frame[0][frame[1].idxmax()])
answer_ls.append("5 - Four By Two Productions")

# 32
data['title_words'] = data['original_title'].apply(lambda x: len(x.split()))
studios_all = data['production_companies'].str.split('|').sum()
studios_unique = np.unique(np.array(studios_all))
word_data = []
for studio in studios_unique:
    mean = data[data['production_companies'].str.contains(studio)]['title_words'].mean()
    word_data.append([studio, mean])
frame = pd.DataFrame(word_data)
print(frame[0][frame[1].idxmax()])
answer_ls.append("5 - Four By Two Productions")

# 33
values = data['original_title'].values
unique_words = []
for v in values:
    words = v.split()
    for word in words:
        unique_words.append(str(word).lower())
words = pd.DataFrame(unique_words)
print(len(words[0].unique()))
answer_ls.append("3 - 2461")

# 34
print(data.sort_values(['vote_average'], ascending=False).head(18))
# print(data.sort_values(['vote_average'], ascending=False).quantile(0.1))
answer_ls.append("1 - Inside Out, Gone Girl, 12 Years a Slave")

# 35
c = collections.Counter()
for actors_list in films['cast'].values:
    actors = []
    for actor in actors_list.split('|'):
        actors.append(actor)
        actors.sort()
        combination = list(combinations(actors, 2))
        for pair in combination:
            c[pair] += 1
print(c.most_common(3))
answer_ls.append("5 - Daniel Radcliffe and Rupert Grint")

# # 36

# Без вариантов ответа не решил до конца эту задачу

# data['profit_value'] = data['revenue'] - data['budget']
# directors_all = data['director'].str.split('|').sum()
# directors_unique = np.unique(np.array(directors_all))
# calculated_data = []
# for director in directors_unique:
#     films = data[data['director'].str.contains(director)]
#     if len(films) > 1:
#         positive_profit = len(films[films['profit_value'] > films['budget']])
#         # positive_profit = len(films[films['revenue'] > films['budget']])
#         positive_percent = ((positive_profit / len(films)) * 100)
#         calculated_data.append([director, positive_percent, len(films), positive_profit])
# frame = pd.DataFrame(calculated_data)
# # # show result
# print(frame[0][frame[1].idxmax()])
# # # show data for visual check
# print(frame)
# answer_ls.append("4 - Christopher Nolan")


answers_frame = pd.DataFrame({'Id': range(1, len(answer_ls)+1), 'Answer': answer_ls}, columns=['Id', 'Answer'])
display(answers_frame)

