import scrapy


class ImageSpider(scrapy.Spider):
    name = "images"
    start_urls = ['https://books.toscrape.com']

    def parse(self, response):
        books = dict()
        image_urls = []
        for book in response.css('article.product_pod'):
            image_urls.append(
                response.urljoin(book.css('div.image_container a img.thumbnail::attr(src)').get()))
        books['image_urls'] = image_urls
        yield books
