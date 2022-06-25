from data import data_manager
from psycopg2 import sql


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


def kamil(order, limit, offset, order_by):
    sql.SQL("""
                SELECT
                    shows.id,
                    shows.title,
                    shows.year,
                    shows.runtime,
                    to_char(shows.rating::float, '999.9') AS rating_string,
                    string_agg(genres.name, ', ' ORDER BY genres.name) AS genres_list,
                    shows.trailer,
                    shows.homepage
                FROM shows
                    JOIN show_genres ON shows.id = show_genres.show_id
                    JOIN genres ON show_genres.genre_id = genres.id
                GROUP BY shows.id
                ORDER BY
                    CASE WHEN %(order)s = 'ASC' THEN {order_by} END ASC,
                    CASE WHEN %(order)s = 'DESC' THEN {order_by} END DESC
                LIMIT %(limit)s
                OFFSET %(offset)s;
            """
            ).format(order_by=sql.Identifier(order_by)),
    {"order": order, "limit": limit, "offset": offset}
