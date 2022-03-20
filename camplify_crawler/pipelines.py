# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import datetime
import os
import sqlite3

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CamplifyCrawlerPipeline:
    _db = None

    @classmethod
    def get_database(cls):
        cls._db = sqlite3.connect(
            os.path.join(os.getcwd(), 'camplify.db'))
        cursor = cls._db.cursor()
        cursor.execute(
            'CREATE TABLE IF NOT EXISTS nap(\
                id INTEGER PRIMARY KEY AUTOINCREMENT, \
                url TEXT UNIQUE NOT NULL, \
                name TEXT NOT NULL);')

        return cls._db

    def process_item(self, entity, spider):
        if entity['name'] == '':
            return entity
        self.save(entity)
        return entity

    def save(self, entity):
        if self.find_by_url(entity['url']):
            return

        db = self.get_database()
        db.execute(
            'INSERT INTO nap (name, url) VALUES (?, ?)', (
                entity['name'],
                entity['url']
            )
        )
        db.commit()

    def find_by_url(self, url):
        db = self.get_database()
        cursor = db.execute(
            'SELECT * FROM nap WHERE url=?',
            (url,)
        )
        return cursor.fetchone()
