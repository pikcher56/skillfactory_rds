from IPython.display import display
import pandas as pd
import collections

data = pd.read_csv('data.csv')

# answers list
answer_ls = []

# # 1
# films = data[data['imdb_id'].isin(['tt1345836', 'tt0413300', 'tt2395427', 'tt1032751', 'tt1298650'])]
# print(films[films['budget'] == films['budget'].max()])
# print(films['imdb_id'][films['budget'].idxmax()])
answer_ls.append("4 - The Warrior's Way (tt1032751)")

# # 2
# films = data[data['imdb_id'].isin(['tt0167260', 'tt0279111', 'tt0360717', 'tt0213149', 'tt0346491'])]
# print(films['imdb_id'][films['runtime'].idxmax()])
answer_ls.append("2 - Gods and Generals (tt0279111)")

# # 3
# films = data[data['imdb_id'].isin(['tt0299172', 'tt0283426', 'tt1449283', 'tt0121164', 'tt0443536'])]
# print(films['imdb_id'][films['runtime'].idxmin()])
answer_ls.append("3 - Winnie the Pooh tt1449283")

# # 4
# print(data['runtime'].mean())
answer_ls.append("2 - 110")

# # 5
# print(data['runtime'].median())
answer_ls.append("1 - 106")

# # 6
# data['profit_value'] = data['revenue'] - data['budget']
# print(data['imdb_id'][data['profit_value'].idxmax()])
answer_ls.append("5 - Avatar tt0499549")

# # 7
# data['profit_value'] = data['revenue'] - data['budget']
# print(data['imdb_id'][data['profit_value'].idxmin()])
answer_ls.append("2 - The Warrior's Way tt1032751")

# # 8
# films = data[data['revenue'] > data['budget']]
# print(len(films))
answer_ls.append("1 - 1478")

# # 9
# films = data.query('release_year == 2008')
# print(films['imdb_id'][films['popularity'].idxmax()])
answer_ls.append("4 - The Dark Knight tt0468569")

# # 10
# data['profit_value'] = data['revenue'] - data['budget']
# films = data.query('release_year == ["2012", "2013", "2014"]')
# print(films['imdb_id'][films['profit_value'].idxmin()])
answer_ls.append("5 - The Lone Ranger tt1210819")

# # 11
# values = data['genres'].values
# unique_genres = []
# for v in values:
#     genres = v.split('|')
#     for genre in genres:
#         unique_genres.append(genre)
# genres = pd.DataFrame(unique_genres)
# print(genres[0].value_counts())
answer_ls.append("3 - Drama")

# # 12
# data['profit_value'] = data['revenue'] - data['budget']
# films = data[data['profit_value'] > 0]
# # print(films)
# values = films['genres'].values
# unique_genres = []
# for v in values:
#     genres = v.split('|')
#     for genre in genres:
#         unique_genres.append(genre)
# genres = pd.DataFrame(unique_genres)
# print(genres[0].value_counts())
answer_ls.append("3 - Drama")

# # 13
# values = data['director'].values
# unique_directors = []
# for v in values:
#     directors = v.split('|')
#     for genre in directors:
#         unique_directors.append(genre)
# directors = pd.DataFrame(unique_directors)
# print(directors[0].value_counts())
answer_ls.append("3 - Steven Soderbergh")

# # 14
# data['profit_value'] = data['revenue'] - data['budget']
# films = data[data['profit_value'] > 0]
# values = films['director'].values
# unique_directors = []
# for v in values:
#     directors = v.split('|')
#     for genre in directors:
#         unique_directors.append(genre)
# directors = pd.DataFrame(unique_directors)
# print(directors[0].value_counts())
answer_ls.append("2 - Ridley Scott ")

# # 15
# data['profit_value'] = data['revenue'] - data['budget']
# grouped_data = data.groupby('director')['profit_value'].sum()
# print(grouped_data.sort_values(ascending=False))
answer_ls.append("5 - Peter Jackson")

# # 16
# data['profit_value'] = data['revenue'] - data['budget']
# actors = ['Emma Watson', 'Johnny Depp', 'Michelle Rodriguez', 'Orlando Bloom', 'Rupert Grint']
# calculated_data = []
# for actor in actors:
#     films = data[data['cast'].str.contains(actor)]
#     profit = films['profit_value'].sum()
#     calculated_data.append([actor, profit])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmax()])
answer_ls.append("1 - Emma Watson")

# # 17
# data['profit_value'] = data['revenue'] - data['budget']
# actors = ['Nicolas Cage', 'Danny Huston', 'Kirsten Dunst', 'Jim Sturgess', 'Sami Gayle']
# calculated_data = []
# for actor in actors:
#     films = data[(data['cast'].str.contains(actor)) & (data['release_year'] == 2012)]
#     profit = films['profit_value'].sum()
#     calculated_data.append([actor, profit])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmin()])
answer_ls.append("3 - Kirsten Dunst")

# # 18
# films = data[data['budget'] > data['budget'].mean()]
# values = films['cast'].values
# unique_actors = []
# for v in values:
#     actors = v.split('|')
#     for actor in actors:
#         unique_actors.append(actor)
# actors = pd.DataFrame(unique_actors)
# print(actors[0].value_counts())
answer_ls.append("3 - Matt Damon")

# # 19
# films = data[data['cast'].str.contains('Nicolas Cage')]
# values = films['genres'].values
# unique_genres = []
# for v in values:
#     genres = v.split('|')
#     for genre in genres:
#         unique_genres.append(genre)
# genres = pd.DataFrame(unique_genres)
# print(genres[0].value_counts())
answer_ls.append("2 - Action")

# # 20
# values = data['production_companies'].values
# unique_companies = []
# for v in values:
#     companies = v.split('|')
#     for genre in companies:
#         unique_companies.append(genre)
# companies = pd.DataFrame(unique_companies)
# print(companies[0].value_counts())
answer_ls.append("1 - Universal Pictures (Universal)")

# # 21
# films = data[data['release_year'] == 2015]
# values = films['production_companies'].values
# unique_companies = []
# for v in values:
#     companies = v.split('|')
#     for genre in companies:
#         unique_companies.append(genre)
# companies = pd.DataFrame(unique_companies)
# print(companies[0].value_counts())
answer_ls.append("4 - Warner Bros")

# # 22
# data['profit_value'] = data['revenue'] - data['budget']
# studios = ['Warner Bros', 'Universal Pictures', 'Columbia Pictures', 'Paramount Pictures', 'Walt Disney']
# calculated_data = []
# for studio in studios:
#     films = data[(data['genres'].str.contains('Comedy')) & (data['production_companies'].str.contains(studio))]
#     profit = films['profit_value'].sum()
#     calculated_data.append([studio, profit])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmax()])
answer_ls.append("2 - Universal Pictures (Universal)")

# # 23
# data['profit_value'] = data['revenue'] - data['budget']
# studios = ['Warner Bros', 'Universal Pictures', 'Columbia Pictures', 'Paramount Pictures', 'Lucasfilm']
# calculated_data = []
# for studio in studios:
#     films = data[(data['production_companies'].str.contains(studio) & (data['release_year'] == 2012))]
#     profit = films['profit_value'].sum()
#     calculated_data.append([studio, profit])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmax()])
answer_ls.append("3 - Columbia Pictures")

# # 24
# data['profit_value'] = data['revenue'] - data['budget']
# films = data[data['production_companies'].str.contains('Paramount Pictures')]
# print(films.sort_values(by=['profit_value']))
answer_ls.append("1 - K-19: The Widowmaker tt0267626")

# # 25
# data['profit_value'] = data['revenue'] - data['budget']
# grouped_data = data.groupby('release_year')['profit_value'].sum()
# print(grouped_data.sort_values(ascending=False))
answer_ls.append("5 - 2015")

# # 26
# data['profit_value'] = data['revenue'] - data['budget']
# films = data[data['production_companies'].str.contains('Warner Bros')]
# grouped_data = films.groupby('release_year')['profit_value'].sum()
# print(grouped_data.sort_values(ascending=False))
answer_ls.append("1 - 2014")

# # 27
# data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
# print(data['month'].value_counts(ascending=False))
answer_ls.append("4 - Сентябрь")

# # 28
# data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
# films = data[data['month'].isin(['6', '7', '8'])]
# print(len(films))
answer_ls.append("2 - 450")

# # 29
# data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
# directors = ['Steven Soderbergh', 'Christopher Nolan', 'Clint Eastwood', 'Ridley Scott', 'Peter Jackson']
# calculated_data = []
# for director in directors:
#     films = len(data[(data['director'].str.contains(director)) & (data['month'].isin(['12', '1', '2']))])
#     calculated_data.append([director, films])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmax()])
answer_ls.append("5 - Peter Jackson")

# # 30
# data['month'] = data['release_date'].apply(lambda x: x.split('/')[0])
# data['year'] = data['release_date'].apply(lambda x: x.split('/')[2])
# data['profit_value'] = data['revenue'] - data['budget']
# year_range = [x for x in range(data['release_year'].min(), data['release_year'].max() + 1)]
# profit_monthes = []
# for year in year_range:
#     films = data[(data['profit_value'] > 0) & (data['year'] == str(year))]
#     grouped = films.groupby('month')['profit_value'].sum().reset_index()
#     month = grouped['month'][grouped['profit_value'].idxmax()]
#     profit_monthes.append(month)
# frame = pd.DataFrame(profit_monthes)
# print(frame[0].value_counts())
answer_ls.append("2 - Июнь")

# # 31
# data['title_length'] = data['original_title'].str.len()
# studios = ['Universal Pictures', 'Warner Bros', 'Jim Henson Company', 'Paramount Pictures', 'Four By Two Productions']
# calculated_data = []
# for studio in studios:
#     films = data[data['production_companies'].str.contains(studio)]
#     title_average_length = films['title_length'].mean()
#     calculated_data.append([studio, title_average_length])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmax()])
answer_ls.append("5 - Four By Two Productions")

# # 32
# data['title_words'] = data['original_title'].apply(lambda x: len(x.split()))
# studios = ['Universal Pictures', 'Warner Bros', 'Jim Henson Company', 'Paramount Pictures', 'Four By Two Productions']
# calculated_data = []
# for studio in studios:
#     films = data[data['production_companies'].str.contains(studio)]
#     title_average_length = films['title_words'].mean()
#     calculated_data.append([studio, title_average_length])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmax()])
answer_ls.append("5 - Four By Two Productions")

# # 33
# values = data['original_title'].values
# unique_words = []
# for v in values:
#     words = v.split()
#     for word in words:
#         unique_words.append(str(word).lower())
# words = pd.DataFrame(unique_words)
# print(len(words[0].unique()))
answer_ls.append("3 - 2461")

# # 34
# print(data.sort_values(['vote_average'], ascending=False).head(18))
answer_ls.append("1 - Inside Out, Gone Girl, 12 Years a Slave")

# # 35
# pairs = [['Johnny Depp', 'Helena Bonham Carter'],
#          ['Hugh Jackman', 'Ian McKellen'],
#          ['Vin Diesel', 'Paul Walker'],
#          ['Adam Sandler', 'Kevin James'],
#          ['Daniel Radcliffe', 'Rupert Grint']
#          ]
# calculated_data = []
# for pair in pairs:
#     actor1 = pair[0]
#     actor2 = pair[1]
#     films = data[(data['cast'].str.contains(actor1)) & (data['cast'].str.contains(actor2))]
#     film_count = len(films)
#     calculated_data.append([pair, film_count])
# frame = pd.DataFrame(calculated_data)
# print(frame[0][frame[1].idxmax()])
answer_ls.append("5 - Daniel Radcliffe and Rupert Grint")

# # 36
# data['profit_value'] = data['revenue'] - data['budget']
# directors = ['Quentin Tarantino', 'Steven Soderbergh', 'Robert Rodriguez', 'Christopher Nolan', 'Clint Eastwood']
# calculated_data = []
# for director in directors:
#     films = data[data['director'].str.contains(director)]
#     positive_profit = len(films[films['profit_value'] > films['budget']])
#     # positive_profit = len(films[films['revenue'] > films['budget']])
#     positive_percent = (positive_profit / len(films)) * 100
#     calculated_data.append([director, positive_percent])
# frame = pd.DataFrame(calculated_data)
# # show result
# print(frame[0][frame[1].idxmax()])
# # show data for visual check
# print(frame)
answer_ls.append("4 - Christopher Nolan")

answers_frame = pd.DataFrame({'Id': range(1, len(answer_ls)+1), 'Answer': answer_ls}, columns=['Id', 'Answer'])
display(answers_frame)

