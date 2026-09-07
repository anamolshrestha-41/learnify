import pandas as pd
import plotly.express as px
data={
       'show_id': [
        's1', 's2', 's3', 's4', 's5',
        's6', 's7', 's8', 's9', 's10',
        's11', 's12', 's13', 's14', 's15'
    ],

    'title': [
        'The Last Kingdom',
        'Stranger Things',
        'The Crown',
        'Extraction',
        'Bird Box',
        'Money Heist',
        'Wednesday',
        'The Irishman',
        'Dark',
        'Our Planet',
        'Red Notice',
        'Narcos',
        'The Witcher',
        'Enola Holmes',
        'Black Mirror'
    ],

    'type': [
        'TV Show', 'TV Show', 'TV Show', 'Movie', 'Movie',
        'TV Show', 'TV Show', 'Movie', 'TV Show', 'TV Show',
        'Movie', 'TV Show', 'TV Show', 'Movie', 'TV Show'
    ],

    'release_year': [
        2015, 2016, 2016, 2020, 2018,
        2017, 2022, 2019, 2017, 2019,
        2021, 2015, 2019, 2020, 2011
    ],

    'rating': [
        'TV-14', 'TV-14', 'TV-MA', 'R', 'R',
        'TV-MA', 'TV-14', 'R', 'TV-MA', 'TV-G',
        'PG-13', 'TV-MA', 'TV-MA', 'PG-13', 'TV-MA'
    ],

    'duration': [
        '4 Seasons', '4 Seasons', '6 Seasons', '117 min', '124 min',
        '5 Seasons', '1 Season', '209 min', '3 Seasons', '8 Episodes',
        '118 min', '3 Seasons', '3 Seasons', '123 min', '5 Seasons'
    ],

    'country': [
        'United Kingdom', 'United States', 'United Kingdom',
        'United States', 'United States', 'Spain', 'United States',
        'United States', 'Germany', 'United States',
        'United States', 'United States', 'United States',
        'United Kingdom', 'United Kingdom'
    ],

    'genre': [
        'Drama', 'Drama', 'Drama', 'Action', 'Horror',
        'Crime', 'Comedy', 'Drama', 'Drama', 'Documentary',
        'Comedy', 'Crime', 'Fantasy', 'Drama', 'Drama'
    ]
}

df= pd.DataFrame(data)

#movies vs tv shows
content_type= df['type'].value_counts()
print(content_type)

#percentage distribution
percentage=(df['type'].value_counts(normalize=True).mul(100).round(2))
print(percentage)

#Visualization
fig= px.bar(df, x='type', title='Distribution of Movies and TV Shows', color='type', y='title')
fig.show()