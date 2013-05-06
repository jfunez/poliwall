AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 5.0
CONCURRENT_REQUESTS_PER_DOMAIN = 1
CONCURRENT_REQUESTS_PER_IP = 0
DOWNLOAD_DELAY = 2    # 250 ms of delay
DOWNLOAD_TIMEOUT = 300

BOT_NAME = 'uy'

SPIDER_MODULES = ['uy.spiders']
NEWSPIDER_MODULE = 'uy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    # 'uy.pipelines.DjangoStoragePipeline',
    'uy.pipelines.DiemDjangoStoragePipeline',
    'uy.pipelines.PoliticianDjangoStoragePipeline',
    'uy.pipelines.PoliticianActionDjangoStoragePipeline',
    'uy.pipelines.PoliticianBiographyDjangoStoragePipeline',
]

DOWNLOAD_TIMEOUT = 60 * 2
