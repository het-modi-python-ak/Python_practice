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
                depth INTEGER,
                snippet TEXT
            )
        """)

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        url = adapter.get("url")
        title = adapter.get("title") or "Unknown"
        depth = adapter.get("depth")
        snippet = adapter.get("snippet") or "No text available"

        self.curr.execute(
            """
            INSERT INTO wiki_pages (url, title, depth, snippet)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(url) DO UPDATE SET
                title = excluded.title,
                depth = excluded.depth,
                snippet = excluded.snippet
            """,
            (url, title, depth, snippet),
        )
        self.conn.commit()
        return item

    def close_spider(self, spider):
        self.conn.close()