import feedparser
from datetime import datetime
from html2text import html2text
from mstations import closest_stations


def remove_all_quotes(s):
    return s.replace('"', '').replace("'", "")


def get_attributes_from_summary(s):
    time = '23:30'
    place = "Nizhnee Zazhopye"
    for el in s.splitlines():
        line = el.strip()
        if line.startswith('**Час:**') or line.startswith('**Время:**') or line.startswith(
                '**Початок:**') or line.startswith('**Дата:**') or line.startswith('**Time:**'):
            time = (line.split("**")[-1]).strip()[:5]
        if line.startswith('**Місце:**') or line.startswith('**Место:**') or line.startswith('**Place:**'):
            place = line.split("**")[-1]
    return time, remove_all_quotes(place.strip())


def check_dou_updates(cursor=None):
    def date_from_string(s):
        currentYear = str(datetime.now().year)
        ua_months = ["січня", "лютого", "березня", "травня", "квітня", "червня", "липня", "серпня", "вересня", "жовтня",
                     "листопада", "грудня"]
        ru_months = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября",
                     "ноября", "декабря"]
        en_months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october",
                     "november", "december"]
        words = s.split(" ")
        day = words[-2].zfill(2)
        strmonth = words[-1].lower()

        try:
            month = ua_months.index(strmonth)
        except(ValueError):
            try:
                month = ru_months.index(strmonth)
            except:
                month = en_months.index(strmonth)
        except:
            return ""
        month = str(month + 1).zfill(2)
        return currentYear + "-" + month + "-" + day

    # what will be, when year changes?

    feed = feedparser.parse(
        'https://dou.ua/calendar/feed/%D0%B2%D1%81%D0%B5%20%D1%82%D0%B5%D0%BC%D1%8B/%D0%9A%D0%B8%D0%B5%D0%B2')
    for el in feed.entries:
        cursor.execute("SELECT EXISTS (SELECT origin FROM events WHERE origin = '{}' LIMIT 1);".format(el.id))
        check = cursor.fetchall()[0][0]
        if check == 1:
            continue

        # rowtitle = el.title
        words = el.title.split(",")
        name = remove_all_quotes(words[-3])
        date = remove_all_quotes(words[-2]).strip()
        print('date len ',len(date.split(" ")), date)
        if len(date.split(" ")) == 3:
            continue  # we don't care about next year
        date = date_from_string(date)
        description = remove_all_quotes(html2text(el.summary))
        start, address = get_attributes_from_summary(description)
        # print(name,description)
        priority = 6
        st = closest_stations(address)

        if cursor:
            sql = f'insert into events (origin,name,date,enddate,time,priority,description,address,source,closest_stations) values ("{el.id}","{name}","{date}","{date}","{start}","{priority}","{description}","{address}","dou","{st}")'
            cursor.execute(sql)


if __name__ == "__main__":
    check_dou_updates(False)
