import scrapy


class DaySpider(scrapy.Spider):
    name = "dayup"
    start_urls = ['http://fund.eastmoney.com/trade/fof.html']

    def parse(self, response):
        if response.url in self.start_urls:
            urls = response.xpath('//*[@id="tblite_fof"]/tbody/tr[1]/td[2]/a/@href').extract()
            name = response.xpath('//*[@id="tblite_fof"]/tbody/tr[1]/td[2]/a/text()').extract()
            for url in urls:
                yield scrapy.Request(url, callback=self.parse)
        else:
            self.parse_detail(response)

    def parse_detail(self, response, parse_eve_detail=False):
        name = response.xpath('//*[@id="body"]/div[11]/div/div/div[1]/div[1]/div/text()').extract_first()
        num = response.xpath('//*[@id="body"]/div[11]/div/div/div[1]/div[1]/div/span[2]/text()').extract_first()
        one_month = response.xpath(
            '//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract_first()
        three_month = response.xpath(
            '//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract_first()
        six_month = response.xpath(
            '//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract_first()
        one_year = response.xpath(
            '//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract_first()

        parts = {}
        for i in range(2, 12):
            part = response.xpath(
                '//*[@id="position_shares"]/div[1]/table/tr[{}]/td[1]/a/text()'.format(i)).extract_first()
            url_page = response.xpath(
                '//*[@id="position_shares"]/div[1]/table/tr[{}]/td[1]/a/@href'.format(i)).extract_first()
            if url_page is not None and parse_eve_detail:
                yield scrapy.Request(url_page, self.eve_parse)
            else:
                parts[part] = url_page
        print(response.url, name, num, parts, one_month)

    def eve_parse(self):
        pass
