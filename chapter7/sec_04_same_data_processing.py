from importFile import *

billboard = pd.read_csv('../doit_pandas/data/billboard.csv')
billboard_long = pd.melt(billboard,
                         id_vars=['year', 'artist', 'track', 'time', 'date.entered'],
                         var_name='week', value_name='rating')
# print(billboard_long.head())

# print(billboard_long[billboard_long.track == 'Loser'].head())

billboard_songs = billboard_long[['year', 'artist', 'track', 'time']]
# print(billboard_songs.shape)

billboard_songs = billboard_songs.drop_duplicates()
# print(billboard_songs.shape)
# print(billboard_songs.head())

billboard_songs['id'] = range(len(billboard_songs))
print(billboard_songs.head(n=10))
