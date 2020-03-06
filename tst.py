a = {
    'description': 'The Neighbourhood їдуть до Києва з масштабним проектop Corn (без сервісного збору) - bit.ly/t/36aSw3M',
    'end_time': '2020-12-02T22:00:00+0200',
    'name': 'The Neighbourhood. 2 грудня, Палац Спорту',
    'place': {'name': 'Палац Спорту',
              'location': {'city': 'Kyiv', 'country': 'Ukraine', 'latitude': 50.43724, 'located_in': '374816775951295',
                           'longitude': 30.52226, 'street': 'Спортивна площа,1', 'zip': '01001'},
              'id': '476591799464322'},
    'start_time': '2020-12-02T19:00:00+0200', 'id': '478624349376056'}

print( a.keys())
# conn = sqlite3.connect('events.db')
#
# #Создаем курсор - это специальный объект который делает запросы и получает их результаты
# cursor = conn.cursor()
# cursor.execute("SELECT EXISTS (SELECT id FROM events WHERE id = '454352' LIMIT 1);")
# results = cursor.fetchall()
# print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
#
# conn.close()

# conn = sqlite3.connect('events.db')
#
# Создаем курсор - это специальный объект который делает запросы и получает их результаты
# cursor = conn.cursor()
# cursor.execute("insert into events (id,date) values (123, '2014-12-12'),(234, '2016-12-12') ")
# conn.commit()
# cursor.execute("SELECT id,date FROM events ORDER BY id")
#
# # Получаем результат сделанного запроса
# results = cursor.fetchall()
# print(results)   # [('A Cor Do Som',), ('Aaron Copland & London Symphony Orchestra',), ('Aaron Goldberg',)]
#
# conn.close()


# import pickledb
# db = pickledb.load('fbevents.db', False)
# for key in db.getall():
#     start = db.get(key)['start_time'][:10]
#     if 'end_time' in db.get(key):
#         end = db.get(key)['end_time'][:10]
#     else:
#         end = 'undefined'
#     print(start, end)
