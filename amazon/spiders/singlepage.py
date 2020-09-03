import scrapy
from ..items import AmazonItem


# call with:
# Scrapy crawl singlepage
class SinglepageSpider(scrapy.Spider):
    name = 'singlepage'
    start_urls = ['https://www.amazon.com/s?i=stripbooks&bbn=549646&rh=n%3A283155%2Cn%3A5%2Cn%3A549646%2Cn%3A3654%2Cp_n_feature_browse-bin%3A2656020011&dc&fst=as%3Aoff&qid=1599090217&rnid=549646&ref=sr_nr_n_2']

    def parse(self, response):
        # call
        items = AmazonItem()
        # Get text with ::text
        product_name = response.css('.a-color-base.a-text-normal::text').extract()
        # Get link with ::attr(src)
        product_link = response.css('.a-spacing-top-small .a-text-bold').css('a::attr(href)').extract()

        # Gets link with ::attr(src)
        product_imagelink = response.css('.s-image::attr(src)').extract()

        product_author = response.css('.sg-col-12-of-28 .a-color-secondary .a-size-base').css('::text').extract()

        # Store the results with these items
        items['product_name'] = product_name
        items['product_link'] = product_link
        items['product_imagelink'] = product_imagelink
        items['product_author'] = product_author

        yield items
