import scrapy

class QuotesSpider(scrapy.Spider):

    # Attributes #
    name = "quotes"
    start_urls = [
        "http://quotes.toscrape.com/"
    ]

    expressions = {
        "getQuotes": '//div[@class="quote"]/span[@class="text"]/text()',
        "getAuthors": '//small[@class="author"]/text()'
    }

    custom_settings = {
        "FEED_EXPORT_ENCODING": "utf-8",
        "FEEDS":
        {
            "quotes.json":
            {
                "format": "json",
                "overwrite": True
            },
            "quotes.csv":
            {
                "format": "csv",
                "overwrite": True
            },
            "quotes.xml":
            {
                "format": "xml",
                "overwrite": True
            }
        }
    }

    # Methods #
    def parse(self, response):

        # Saves the html of the web in a file #
        with open("quotes-web.html", "w", encoding="utf-8") as file:
            file.write(response.text)
        
        # Gets the quotes #
        quotes = response.xpath('//div[@class="quote"]/span[@class="text"]/text()').getall()

        # Gets the authors #
        authors = response.xpath('//small[@class="author"]/text()').getall()

        # Returns the scrapped info #
        yield {
            "quotes": quotes,
            "authors": authors
        }

        # Gets the link of the next page #
        nextPage = response.xpath('//ul[@class="pager"]/li[@class="next"]/a/@href').get()

        # Go to the next page and repeat the function #
        if nextPage:
            yield response.follow(nextPage, self.parse)