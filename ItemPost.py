import datetime
import string
from feapder import Item


class ItemPost(Item):

    # __unique_key__ = ["title", "url"]

    def __init__(self, *args, **kwargs):
        self.table_name = "Post"
        self.board = string
        self.title = string
        self.url = string
        self.author = string
        self.mark = string
        self.post_time = datetime.datetime

    def pre_to_db(self):
        """
        入库前的处理
        """
        self.title = self.title.strip()
