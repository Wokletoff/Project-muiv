import sqlite3
import sys
from settings import settings

class Database:

    def __init__(self):
        self.sqlite_connection = sqlite3.connect('base_map.db')
        self.map_list = [(1, "img/height_map.jpg", "img/color_map.jpg"),
                         (2, "img/height_map_1.png", "img/color_map_1.png"),
                         (3, "img/map04.jpg", "img/mapcol04.jpg")]

    def create_base(self):
        try:
            sqlite_create_table_query = '''CREATE TABLE base_map (
                                        id INTEGER PRIMARY KEY,
                                        map_hight TEXT NOT NULL,
                                        map_color TEXT NOT NULL );'''
            cursor = self.sqlite_connection.cursor()
            print("База данных подключена к SQLite")
            cursor.execute(sqlite_create_table_query)
            self.sqlite_connection.commit()
            print("Таблица SQLite создана")

            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при подключении к sqlite", error)

    def info_base(self, records):
        try:

            cursor = self.sqlite_connection.cursor()
            print("Подключен к SQLite")

            sqlite_insert_with_param = """INSERT INTO base_map
                                         (id, map_hight, map_color)
                                         VALUES (?, ?, ?);"""

            cursor.executemany(sqlite_insert_with_param, records)
            self.sqlite_connection.commit()
            print ("Запись успешно вставлена ​​в таблицу base_map ", cursor.rowcount)
            self.sqlite_connection.commit()
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite:", error)

    def pars_base(self, developer_id, what_map):

            cursor = self.sqlite_connection.cursor()
            sqlite_select_query = """SELECT * from base_map where id = ?"""
            cursor.execute(sqlite_select_query, (developer_id,))
            record = cursor.fetchone()
            return record[what_map]

    def run(self):
        self.pars_base(settings.int_map, 2)


if __name__ == "__main__":
    db = Database()
    db.run()