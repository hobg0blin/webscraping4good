# Web Scraping For Better Datasets

To get the most out of this workshop, you’ll need to have [python](https://www.python.org/downloads/) and [scrapy](https://scrapy.org/) installed. If you haven’t used python before, we’re going to start with the simplest possible applications of it, so you should be able to follow along. If this ends up sparking your fancy, there are tons of resources available online, some of my favorites of which are linked on the workshop’s [are.na](https://www.are.na/brent-bailey/web-scraping-4-social-good).

## What’s web scraping?

Simply put, it’s gathering and extracting data from a website or websites. If you’ve ever saved a meme from a website or copied and pasted text from an article, congrats! You’re a web scraper.

Generally, however, what people mean when they talk about web scraping is the automation of this process. Rather than manually searching flickr for pictures of trees and downloading them one by one, automated web scraping allows us to download every picture of a tree on flickr in a short amount of time by executing simple scripts or using software.

## What do people use it for?

## What tools can we use to scrape data?

### Basic

[wget] :

### High-Level

There are a whole lot of them, and you can also write your own! We’re going to focus primarily on scraping with Python, so here are a few of the most popular scraping tools.

[Scrapy](https://scrapy.org/): Python. High level, easy to use. Sometimes needs to be used with Selenium or Beautiful Soup for websites with a lot of dynamic content.
Good for crawling websites - visiting multiple pages in a single session. Extremely fast and extensible.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/): Python. The OG scraper, old, good for parsing HTML, lower level.

[Selenium](https://github.com/SeleniumHQ/selenium): APIs for a number of languages. Often used for web automation or testing. Works well with JavaScript and dynamic content - better at mimicking the way we actually interact with websites.

## Let’s write a scraper!

If you haven’t already, let’s install Scrapy. You can do this easily in the terminal with ```pip install scrapy```.


