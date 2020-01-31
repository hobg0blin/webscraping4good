import scrapy


class TextSpider(scrapy.Spider):
    name = "text"

    def start_requests(self):
        # tell it which website(s) to visit
        urls = ['http://books.toscrape.com']
        # visit each url
        for url in urls:
            # at each url, run the ‘parse’ function
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # set a filename to write the response to
        filename = 'books.html'
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log('Saved file % s' % filename)
