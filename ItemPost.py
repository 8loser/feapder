import datetime
import string
from feapder import Item

import pytz


class ItemPost(Item):
    __unique_key__ = ["url"]
    tw = pytz.timezone('Asia/Taipei')

    def __init__(self, *args, **kwargs):
        self.table_name = "Post"
        self.board = string
        self.title = string
        self.url = string
        self.author = string
        self.mark = string
        self.post_time = datetime.datetime

    def pre_to_db(self):
        self.title = self.title.strip()
        self.url = self.url.strip()
        self.author = self.author.strip()
        self.mark = self.mark.strip() if self.mark else self.mark
        self.post_time = self.tw.localize(self.post_time)
