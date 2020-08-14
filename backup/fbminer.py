import facebook


def cache_events(token, userid="10156265228397361"):
    token = "EAAcN8pRZBfnQBAKiFZAzFifP1jSV7gsVRErt3milnhMO9H2EgZBBxyciwH1z4MhqygtSo3OQVO1QG6RkBlbSdZCsg4umX7m7UvLPonZAk8q8GEfjjNhF9S4ZB8Ksl7H5KKOqCAdOr14xpxhmfKFUvBibMzD21RCAfqQTQnZAZBZAHSB8sh4QZCr9A3eybYPHSXZCdvyzOJs3DK3ZAwZDZD"
    graph = facebook.GraphAPI(access_token=token, version="2.8")
    rez = graph.get_all_connections(id=userid, connection_name='events')
    print(rez)
    c = 0
    for event in rez:
        c += 1
        print(event)
        break
    print(c)  # 223

    exit()


# https://github.com/patx/pickledb
import pickledb

db = pickledb.load('fbevents.db', False)

for event in rez:
    db.set(event["id"], event)

db.dump()

db = pickledb.load('fbevents.db', False)
print(len(db.getall()))
