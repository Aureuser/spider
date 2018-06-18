# -*- coding: utf-8 -*-
# 项目的设置文件
# Scrapy settings for ITcase project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
# 为简单起见，该文件仅包含被认为重要的设置或
# 常用。你可以找到更多的设置咨询文档：
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ITcase'

SPIDER_MODULES = ['ITcase.spiders']
NEWSPIDER_MODULE = 'ITcase.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#通过在用户代理上标识自己（和您的网站）负责任地进行爬网
#USER_AGENT = 'ITcase (+http://www.yourdomain.com)'

# Obey robots.txt rules
#遵守robots.txt规则
# ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# 配置Scrapy执行的最大并发请求（默认值：16）
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 为同一网站的请求配置延迟（默认值：0）
# 请参阅https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# 另请参阅自动油门设置和文档
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 下载延迟设置将只符合以下之一：
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# 禁用Cookie（默认启用)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# 禁用Telnet控制台（默认启用）相当于监控
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# 覆盖默认的请求标头：
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# 启用或禁用爬虫中间件
# 请参阅https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ITcase.middlewares.ItcaseSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# 启用或禁用下载器中间件
# 见https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ITcase.middlewares.ItcaseDownloaderMiddleware': 543,#0-1000值越小优先级越高
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# 启用或禁用扩展
# 请参阅https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 配置项目管道
# 请参阅https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {#管道文件
   'ITcase.pipelines.ItcasePipeline': 300,#值越小优先级越高
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# 启用并配置AutoThrottle扩展名（默认情况下禁用）
# 请参阅https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 最初的下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 在高延迟情况下设置的最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# Scrapy应平行发送的请求的平均数量
# 每个远程服务器
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 为每个收到的响应启用显示限制统计信息：
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 启用并配置HTTP缓存（默认情况下禁用）
# 请参阅https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
