import sys

BOT_NAME = 'poliwall'

SPIDER_MODULES = ['poliwall.spiders']
NEWSPIDER_MODULE = 'poliwall.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    #'poliwall.pipelines.DjangoStoragePipeline',
]