import scrapy

class PostSpider(scrapy.Spider):
    name = "posts"

    start_urls = [
        'https://blog.scrapinghub.com/'
    ]

    def parse(self, response):
       
        #default function used to process the downloaded responses,returning the scape data
        #response is the data that we scape

        #the following code scraps the html of the page
        #page = response.url.split('/')[-1]  #getting the page number
        #filename = 'posts-%s.html'%page
        #with open(filename,'wb') as f:
        #    f.write(response.body)

        #the following code scraps the useful elements of the page and stores in a json format
        #run the command 'scrapy crawl posts -o posts.json'

        for post in response.css('div.post-item'):
            #crawls the page 1
            yield{
                'title': post.css('.post-header h2 a::text')[0].get(),
                'date': post.css('.post-header a::text')[1].get(),
                'author': post.css('.post-header a::text')[2].get(),
            }

        #go to the next page following a link
        #scraps the entire site
        next_page = response.css('a.next-post-link::attr(href)').get()
        
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)