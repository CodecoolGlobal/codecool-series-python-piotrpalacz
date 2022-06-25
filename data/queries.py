from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows(offset=0, limit=15):
    return data_manager.execute_select("""
    SELECT shows.id, title, year, runtime, to_char(rating::float, '999.9') as rating,string_agg(genres.name, ', ')As genres ,trailer, homepage
    FROM shows
    INNER JOIN show_genres ON shows.id = show_genres.show_id
    INNER JOIN genres ON show_genres.genre_id = genres.id
    GROUP BY shows.id
    ORDER BY rating DESC LIMIT %(limit)s OFFSET %(offset)s
    """, {'limit':limit, 'offset': offset})


def get_shows_page_count(page=15):
    return data_manager.execute_select("""
    SELECT count(*) / %(page)s AS page_count
    FROM shows
    """, {'page': page})

