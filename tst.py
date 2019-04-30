import pickledb
db = pickledb.load('fbevents.db', False)
for key in db.getall():
    start = db.get(key)['start_time'][:10]
    if 'end_time' in db.get(key):
        end = db.get(key)['end_time'][:10]
    else:
        end = 'undefined'
    print(start, end)