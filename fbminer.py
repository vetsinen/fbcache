import facebook
token = "EAAcN8pRZBfnQBAI57yzUSICdtHrc6ClGONqvpwsfLjZCNKCxv6yPicr5Ew6jk9DYGZA07H5zlNi1mjiMErY7eTgD6mx6OwY2gBZA5nM2hxIIPSXyzvuw3x7CZAEI4LwKQ0uZBc7fXarGZCrcs5OTp2YDxxOlg30T7N2yKeA5jSZBrW6JbAzRVdOTug9uEqZBMwKIZD"
#experimental token
token = "EAAcN8pRZBfnQBAAMgJcab09ro0XhlJnusRA8wdGDMLsUmvJDeULgGyOY3oxxirYewKbnIVPYq7ZBjxShoUa6eB6ZBfa97EpieRYOfIkP24dztl0f3VLTk8tNRoUhiMZAHj9c6nCLzTkYANNEHq6clHGovMLYNCLLOmIOlJwaB479DyWO1AmkZCDDFcSaXPNCntQJjIZCjGCgZDZD"
userid = "10156265228397361"
graph = facebook.GraphAPI(access_token=token, version="2.8")
rez = graph.get_all_connections(id=userid, connection_name='events')
print(rez)
c=0
for event in rez:
    c+=1
    print(event)
    break
print(c) #223

exit()

# https://github.com/patx/pickledb
import pickledb
db = pickledb.load('fbevents.db', False)

for event in rez:
    db.set(event["id"],event)

db.dump()

db = pickledb.load('fbevents.db', False)
print(len(db.getall()))