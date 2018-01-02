# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

ITEM_PIPELINES = {
        'top_albums.pipelines.TopAlbumPipeline':500
        }

BOT_NAME = 'tutorial'

SPIDER_MODULES = ['top_albums.spiders']
NEWSPIDER_MODULE = 'top_albums.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'
