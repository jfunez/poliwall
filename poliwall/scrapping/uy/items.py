# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class Deputy(Item):
    first_name = Field()
    last_name = Field()
    party = Field()
    state = Field()
    email = Field()
    photo_url = Field()
    profile_url = Field()
    politician_id = Field()


class Senator(Item):
    first_name = Field()
    last_name = Field()
    party = Field()
    email = Field()
    photo_url = Field()
    profile_url = Field()
    politician_id = Field()


class Action(Item):
    date = Field()
    text = Field()
    politician_id = Field()
    source_url = Field()
