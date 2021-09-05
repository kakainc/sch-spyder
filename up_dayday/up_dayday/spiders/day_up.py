import scrapy


class DaySpider(scrapy.Spider):
    name = "dayup"
    start_urls = ['http://fund.eastmoney.com/trade/fof.html']

    def parse(self, response):
        if response.url in self.start_urls:
            urls = response.xpath('//*[@id="tblite_fof"]/tbody/tr[1]/td[2]/a/@href').extract()
            print(urls)
            name = response.xpath('//*[@id="tblite_fof"]/tbody/tr[1]/td[2]/a/text()').extract()
            print(name)
            for url in urls:
                yield scrapy.Request(url, callback=self.parse)
        else:
            self.parse_detail(response)

    def parse_detail(self, response):
        name = response.xpath('//*[@id="body"]/div[11]/div/div/div[1]/div[1]/div/text()').extract()[0]
        num = response.xpath('//*[@id="body"]/div[11]/div/div/div[1]/div[1]/div/span[2]/text()').extract()[0]
        # parts = []
        part = response.xpath(
            '/html/body/div[2]/div[13]/div/div/div[1]/div[2]/div[2]/ul/li[1]/div[1]/table/tbody/tr[2]/td[1]/a/@href').extract()
        # for i in range(2, 12):
        #     part = response.xpath('//*[@id="position_shares"]/div[1]/table/tbody/tr[2]/td[1]/a/text()').extract()
        #     parts.append(part)
        print(response.url, name, num, part)
