BOT_NAME = 'fixstay'

SPIDER_MODULES = ['fixstay.spiders']
NEWSPIDER_MODULE = 'fixstay.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'INFO'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'fixstay.pipelines.FixstayPipeline': 100,

}