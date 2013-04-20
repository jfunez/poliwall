import djcelery
djcelery.setup_loader()

BROKER_URL = 'django://'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'
