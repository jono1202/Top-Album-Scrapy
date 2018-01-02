import scrapy
from top_albums.items import TopAlbum

class TopAlbumSpider(scrapy.Spider):
    name = 'topalbum'

    start_urls = ['https://www.rollingstone.com/music/lists/500-greatest-albums-of-all-time-20120531/outkast-aquemini-20120525']

    def parse(self, response): 
        '''
        self.log('Saved file %s' % filename)
        self.log('Title %s' % response.xpath('/html/head/title/text()').extract_first())
        self.log('Description %s' % response.xpath('/html/head/meta[@name="description"]/@content').extract_first())
        self.log('Index %s' % response.xpath('//*[@id="collection-items-container"]/h2/span/text()').extract_first())
        self.log('Next URL %s' % response.xpath('/html/head/link[@rel="next"]/@href').extract_first())
        '''

        rawTitle = response.xpath('//*[@id="collection-items-container"]/h2/text()').extract_first()
        rawDescription = response.xpath('/html/head/meta[@name="description"]/@content').extract_first()
        rawIndex = response.xpath('//*[@id="collection-items-container"]/h2/span/text()').extract_first()
        rawYearAndLabel = response.xpath('//*[@id="collection-items-container"]/div[1]/p[1]/em/text()').extract_first()

        artist = rawTitle[1:rawTitle.find(" '")-1]
        title = rawTitle[rawTitle.find(" '")+2:len(rawTitle)-1] 
        
        index = int(rawIndex.rstrip('.'))
        
        try:
            year = int(rawDescription.split(',',1)[1].lstrip().split(' ',1)[0])
            label = rawDescription.split(',',1)[0]
            if index == 1: 
                description = rawDescription.split(',',1)[1].lstrip().split(' ',1)[1]
                description = description[0:description.find("Voters:")].strip()
            else:
                description = rawDescription.split(',',1)[1].lstrip().split(' ',1)[1]
                description = description[0:len(description)-1].strip()
        except ValueError:
            description = rawDescription
            year = None
            label = None
        
        yield TopAlbum(
            index = index,
            title = title,
            artist = artist,
            label = label,
            year = year,
            description = description
        )
        
        next_url = response.xpath('/html/head/link[@rel="next"]/@href').extract_first()
        if next_url is not None:
            yield scrapy.Request(next_url, callback=self.parse)
