BOT_NAME = 'uy'

SPIDER_MODULES = ['uy.spiders']
NEWSPIDER_MODULE = 'uy.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    # 'uy.pipelines.DjangoStoragePipeline',
    'uy.pipelines.DiemDjangoStoragePipeline',
    'uy.pipelines.PoliticianDjangoStoragePipeline',
    'uy.pipelines.PoliticianBiographyDjangoStoragePipeline',
]
