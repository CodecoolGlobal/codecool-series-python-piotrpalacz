from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows():
    return data_manager.execute_select(
        """
        SELECT title, year, runtime, trailer, homepage, shows.id, rating,string_agg(genres.name, ', ')
        FROM shows
        INNER JOIN show_genres ON shows.id = show_genres.id
        INNER JOIN genres ON show_genres.genre_id = genres.id
        GROUP BY shows.id
        ORDER BY rating DESC LIMIT 15
        """)

