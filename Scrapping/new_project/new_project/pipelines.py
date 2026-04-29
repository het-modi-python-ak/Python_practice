# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import sqlite3
from itemadapter import ItemAdapter


class SqlitePipeline:
    def __init__(self):
        self.conn = sqlite3.connect("wiki_scraping.db")
        self.curr = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.curr.execute("""
            CREATE TABLE IF NOT EXISTS wiki_pages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                url TEXT UNIQUE,
                title TEXT,
                depth INTEGER
            )
        """)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        url = adapter.get("url")
        title = adapter.get("title") or "Unknown"
        depth = adapter.get("depth")

        self.curr.execute(
            """
            INSERT INTO wiki_pages (url, title, depth)
            VALUES (?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
                title = excluded.title,
                depth = excluded.depth
            """,
            (url, title, depth),
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()