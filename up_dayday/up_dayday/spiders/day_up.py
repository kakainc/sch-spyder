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
        one_month = \
            response.xpath('//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract()
        three_month = response.xpath('//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()')
        six_month = \
            response.xpath('//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract()
        one_year = \
            response.xpath('//*[@id="body"]/div[11]/div/div/div[2]/div[1]/div[1]/dl[1]/dd[2]/span[2]/text()').extract()



        parts = {}
        for i in range(2, 12):
            part = response.xpath('//*[@id="position_shares"]/div[1]/table/tr[{}]/td[1]/a/text()'.format(i)).extract()[0]
            url = response.xpath('//*[@id="position_shares"]/div[1]/table/tr[{}]/td[1]/a/@href'.format(i)).extract()[0]
            parts[part] = url
        print(response.url, name, num, parts)
