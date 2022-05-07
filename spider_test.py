import feapder


class SpiderTest(feapder.AirSpider):

    def start_requests(self):
        for i in range(1, 2):
            yield feapder.Request(
                "https://www.ptt.cc/bbs/Gossiping/index{}.html".format(i))

    def download_midware(self, request):
        request.headers = {"Cookie": "over18=1"}
        return request

    def parse(self, request, response):
        article_list = response.xpath('//div[@class="title"]')
        for article in article_list:
            title = article.xpath("./a/text()").extract_first()
            url = article.xpath("./a/@href").extract_first()
            print(title, url)

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
    SpiderTest().start()
