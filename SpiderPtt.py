from datetime import datetime
import feapder
# from feapder.db.mongodb import MongoDB
from feapder import Item

from ItemPost import ItemPost


class SpiderPtt(feapder.AirSpider):
    __custom_setting__ = dict(
        ITEM_PIPELINES=["feapder.pipelines.mongo_pipeline.MongoPipeline"],
        MONGO_IP="mongo",
        MONGO_PORT=27017,
        MONGO_DB="db",
        MONGO_USER_NAME="admin",
        MONGO_USER_PASS="pass",
    )

    def start_requests(self):
        yield feapder.Request(
            "https://www.ptt.cc/bbs/Gossiping/index39308.html",
            callback=self.parse_post)
        # yield feapder.Request("https://www.ptt.cc/bbs/Gossiping/index.html",
        #                       callback=self.parse_post)

        # for i in range(1, 2):
        # yield feapder.Request(
        #     "https://www.ptt.cc/bbs/Gossiping/index{}.html".format(i))

    def download_midware(self, request):
        request.headers = {"Cookie": "over18=1"}
        return request

    def parse_post(self, request, response):
        '''
        解析 post 資料
        '''
        post_list = response.xpath('//div[@class="r-ent"]')
        for post in post_list:
            title_div = post.xpath('./div[@class="title"]')
            title = title_div.xpath('./a/text()').extract_first()
            # 文章被刪除會找不到 title，忽略繼續下一筆
            if (title is None):
                continue

            url = title_div.xpath('./a/@href').extract_first()
            meta_div = post.xpath('./div[@class="meta"]')
            author = meta_div.xpath(
                './div[@class="author"]/text()').extract_first()
            mark = meta_div.xpath(
                './div[@class="mark"]/text()').extract_first()
            # 取得網址後繼續解析post詳細資料
            yield feapder.Request(url,
                                  callback=self.parse_post_detail,
                                  title=title,
                                  author=author,
                                  mark=mark)

    def parse_post_detail(self, request, response):
        # 產生 post 資料
        board = response.xpath('//a[@class="board"]/text()[1]').extract_first()
        title = request.title
        url = request.url
        author = request.author
        mark = request.mark
        post_time_str = response.xpath(
            "//div[@class='article-metaline'][3]/span[@class='article-meta-value'][1]/text()[1]"
        ).extract_first()
        post_time = datetime.strptime(post_time_str, '%a %b %d %H:%M:%S %Y')

        item = ItemPost()
        item.board = board
        item.title = title
        item.url = url
        item.author = author
        item.mark = mark
        item.post_time = post_time
        yield item

    def parse_detail(self, request, response):
        """
        解析详情
        """
        # 取url
        url = request.url
        # 取title
        title = request.title
        # 解析正文
        content = response.xpath(
            'string(//div[@class="content"])').extract_first(
            )  # string 表达式是取某个标签下的文本，包括子标签文本

        print("url", url)
        print("title", title)
        print("content", content)


if __name__ == "__main__":
    SpiderPtt().start()
