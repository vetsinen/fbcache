

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
