import feapder
# from feapder.db.mongodb import MongoDB
from feapder import Item


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
        yield feapder.Request("https://www.ptt.cc/bbs/Gossiping/index.html",
                              callback=self.parse_post)
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
            url = title_div.xpath('./a/@href').extract_first()
            meta_div = post.xpath('./div[@class="meta"]')
            author = meta_div.xpath(
                './div[@class="author"]/text()').extract_first()
            mark = meta_div.xpath(
                './div[@class="mark"]/text()').extract_first()
            item = Item()
            item.table_name = "post"
            item.title = title
            item.url = url
            item.author = author
            if (mark is not None):
                item.mark = mark
            yield item

        # yield feapder.Request(url, callback=self.parse_detail,
        #                       title=title)  # callback 为回调函数

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
