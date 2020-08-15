a = {'accuracy': 0.401,
     'address': 'бульвар Вацлава Гавела, Миколи Василенка вулиця, Грушки, Відрадний, Київ, Солом’янський район, 03024, Україна',
     'bbox': {'northeast': [50.4471158, 30.4201457], 'southwest': [50.4470158, 30.4200457]}, 'city': 'Київ',
     'confidence': 10, 'country': 'Україна', 'country_code': 'ua',
     'icon': 'https://nominatim.openstreetmap.org/images/mapicons/transport_tram_stop.p.20.png', 'importance': 0.401,
     'lat': 50.4470658, 'lng': 30.4200957, 'ok': True, 'osm_id': 1465727588, 'osm_type': 'node', 'place_id': 15711857,
     'place_rank': 30, 'postal': '03024', 'quality': 'tram_stop', 'quarter': 'Грушки',
     'raw': {'place_id': 15711857, 'licence': 'Data © OpenStreetMap contributors, ODbL 1.0. https://osm.org/copyright',
             'osm_type': 'node', 'osm_id': 1465727588,
             'boundingbox': ['50.4470158', '50.4471158', '30.4200457', '30.4201457'], 'lat': '50.4470658',
             'lon': '30.4200957',
             'display_name': 'бульвар Вацлава Гавела, Миколи Василенка вулиця, Грушки, Відрадний, Київ, Солом’янський район, 03024, Україна',
             'place_rank': 30, 'category': 'railway', 'type': 'tram_stop', 'importance': 0.401,
             'icon': 'https://nominatim.openstreetmap.org/images/mapicons/transport_tram_stop.p.20.png',
             'address': {'railway': 'бульвар Вацлава Гавела', 'road': 'Миколи Василенка вулиця', 'quarter': 'Грушки',
                         'suburb': 'Відрадний', 'city': 'Київ', 'borough': 'Солом’янський район', 'postcode': '03024',
                         'country': 'Україна', 'country_code': 'ua'}}, 'status': 'OK',
     'street': 'Миколи Василенка вулиця', 'suburb': 'Відрадний', 'type': 'tram_stop'}

print(a.keys())
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
