def get_songs_in_year(df, year):
    mask = df.year.apply(lambda x: x == int(year))
    return df[mask]