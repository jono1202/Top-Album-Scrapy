# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import psycopg2

class TopAlbumPipeline(object):
    def __init__(self):
        import psycopg2
        self.conn = psycopg2.connect(user="postgres",
                dbname="scrape", 
                password="password", 
                host='127.0.0.1',
                port='5432')
        self.conn.cursor().execute(
                """delete from top_albums where index > -1""")

    def process_item(self, item, spider):
        cur = self.conn.cursor();
        cur.execute(
                """insert into top_albums 
                (index, title, artist, year, label, description)
                values
                (%s, %s, %s, %s, %s, %s)""",
                (
                    item['index'],
                    item['title'],
                    item['artist'],
                    item['year'],
                    item['label'],
                    item['description']
                )
                )
        self.conn.commit()
        return item
