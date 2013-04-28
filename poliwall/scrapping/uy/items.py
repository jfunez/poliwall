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
    role = Field()


class Politician(Item):
    first_name = Field()
    last_name = Field()
    party = Field()
    email = Field()
    photo_url = Field()
    profile_url = Field()
    role = Field()
    politician_id = Field()
    legislative_id = Field()
    state = Field()
    profile_id = Field()
    biography = Field()


class Diem(Item):
    first_name = Field()
    last_name = Field()
    type = Field()
    party = Field()
    date = Field()
    extra = Field()
    number = Field()
    ol = Field()
    place = Field()
    event = Field()
    days = Field()
    start_date = Field()
    end_date = Field()
    ticket_cost = Field()
    travel_insurance = Field()
    diem = Field()
    report_refund = Field()
    report_date = Field()
    report_rest = Field()
    total_trip = Field()
    observations = Field()
