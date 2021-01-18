import sqlite3


class FixstayPipeline:
    conn = sqlite3.connect('fixstay.db')
    cursor = conn.cursor()

    def open_spider(self, spider):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS `fixstay` (
                                        title varchar(100),
                                        description text
                                        )''')
        self.conn.commit()

    def process_item(self, item, spider):
        title = item['title'][0]
        description = item['description'][0]
        print(title)

        self.cursor.execute(f"""select * from fixstay where title = '{title}'""")
        is_exist = self.cursor.fetchall()

        if len(is_exist) == 0:
            self.cursor.execute(f"""insert into `fixstay`
                                    (`title`, `description`)
                                    values (?, ?)""", (title, description))
            self.conn.commit()

        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()