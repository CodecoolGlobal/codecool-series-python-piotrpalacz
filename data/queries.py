from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')
