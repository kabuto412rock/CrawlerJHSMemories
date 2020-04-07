# -*- coding: utf-8 -*-
import scrapy
class MemoriesSpider(scrapy.Spider):
    name = 'memories'
    start_urls=[
        'http://tw.class.uschoolnet.com/class/?csid=css000000107823&id=model8&cl=1273127232-3234-3471',
        ]
    
    def parse(self, response):
        td1s = response.css('td.j8monster_row2_1')
        for some_td in td1s:
            relative_url = some_td.css('td')[0].css('a::attr(href)').get()
            some_td_non_empty_texts = list(map(lambda s : s.strip() if len(s.strip()) > 1 else '', some_td.css('::text').getall()))
            title = ''.join(some_td_non_empty_texts)
            # photo_count = int(title.split('共')[1].split('張')[0].strip())
            
            yield response.follow(relative_url,  callback=self.parse_album_pages, meta={'directory':title})
            # yield {
            #     'link': response.urljoin(relative_url),
            #     'title': title,
            # }
            
        td2s = response.css('td.j8monster_row2_2')
        for some_td in td2s:
            relative_url = some_td.css('td')[0].css('a::attr(href)').get()
            some_td_non_empty_texts = list(map(lambda s : s.strip() if len(s.strip()) > 1 else '', some_td.css('::text').getall()))
            title = ''.join(some_td_non_empty_texts)
            # photo_count = int(title.split('共')[1].split('張')[0].strip())
            yield response.follow(relative_url,  callback=self.parse_album_pages, meta={'directory':title})

            
    def parse_album_pages(self, response):
        directory = response.meta['directory']
        img_links= response.css('td.album_td_blue a::attr(href)').getall()
        next_page_link = response.xpath('//a[contains(text(), "下一頁")]/@href').get()
        for img_link in img_links:
            yield {directory: img_link}
        if next_page_link is not None:
            yield response.follow(next_page_link, callback=self.parse_album_pages, meta={"directory": directory})
        
        