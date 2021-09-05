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

    def parse_detail(self, response):
        name = response.xpath('//*[@id="position_shares"]/div[1]/table/tbody/tr[2]/td[1]/a/text()').extract()

        scale = response.xpath(
            '//*[@id="body"]/div[4]/div[9]/div/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[2]/text()').extract()
        ttt = response.xpath('//*[@id="highcharts-24"]/svg/g[5]/g[3]/rect[4]/@height').extract()
        # print (response.url, name, nh_shouyi, start_date, scale, ttt)
        print('{};;{};;{};;{};;{};;{}'.format(name[0], response.url, nh_shouyi[0], start_date[0], scale[0], ttt[0]))
