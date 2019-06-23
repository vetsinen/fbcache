import geocoder
from math import radians, sin, cos, acos

stations = (
'Akademmistechko', 'Zhytomyrska', 'Sviatoshyn', 'Nyvky', 'Beresteiska', 'Shuliavska', 'Politekhnichnyi Instytut',
'Vokzalna', 'Universytet', 'Teatralna', 'Khreshchatyk', 'Arsenalna', 'Dnipro', 'Hidropark', 'Livoberezhna', 'Darnytsia',
'Chernihivska', 'Lisova', 'Heroiv Dnipra', 'Minska', 'Obolon', 'Pochaina', 'Tarasa Shevchenka (Kiev Metro)',
'Kontraktova Ploshcha', 'Poshtova Ploshcha', 'Maidan', 'Ploshcha Lva Tolstoho', 'Olimpiiska', 'Palats Ukrayina',
'Lybidska', 'Demiivska', 'Holosiivska', 'Vasylkivska', 'Vystavkovyi Tsentr', 'Ipodrom', 'Teremky', 'Syrets',
'Dorohozhychi', 'Lukianivska', 'Zoloti Vorota', 'Palats Sportu', 'Klovska', 'Pecherska', 'Druzhby Narodiv', 'Vydubychi',
'Slavutych', 'Osokorky', 'Pozniaky', 'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'Chervony Khutir')
shorts = (
'Akademka', 'Zhyto', 'Sviatoshyn', 'Nyvky', 'Beresta', 'Shuliavska', 'Politeh', 'Vokzal', 'Univer', 'Teatralna',
'Khreshchatyk', 'Arsenalna', 'Dnipro', 'Hidropark', 'Livober', 'Darnytsia', 'Cherniha', 'Lisova', 'HeroiD', 'Minska',
'Obolon', 'Pochaina', 'Shevchenka', 'Kontraktova', 'Poshtova', 'Maidan ', 'Tolstoho', 'Olimpiiska', 'PUkrayina',
'Lybidska', 'Demiivska', 'Holoseyka', 'Vasylkivska', 'Vystavka', 'Ipodrom', 'Teremky', 'Syrets', 'Dorohozhychi',
'Lukianivska', 'Zoloti', 'PSportu', 'Klovska', 'Pecherska', 'Druzhby', 'Vydubychi', 'Slavutych', 'Osokorky', 'Pozniaky',
'Kharkivska', 'Vyrlytsia', 'Boryspilska', 'CheKhutir')

# coords = {station:geocoder.arcgis('Kyiv, metro '+station).latlng for station in stations}
coords = {'Akademka': [50.46656000000007, 30.355720000000076], 'Zhyto': [50.45595000000003, 30.364670000000046],
          'Sviatoshyn': [50.457760000000064, 30.39124000000004], 'Nyvky': [50.48705000000007, 30.51818000000003],
          'Beresta': [50.45851000000005, 30.41892000000007], 'Shuliavska': [50.45474000000007, 30.445130000000063],
          'Politeh': [50.451050000000066, 30.46655000000004], 'Vokzal': [50.441730000000064, 30.488530000000026],
          'Univer': [50.444127, 30.5026766], 'Teatralna': [50.445150026112174, 30.519030003895214],
          'Khreshchatyk': [50.44740000000007, 30.521980000000042], 'Arsenalna': [50.44378000000006, 30.54529000000008],
          'Dnipro': [50.52260000000007, 30.49794000000003], 'Hidropark': [50.446885500000015, 30.576291750000017],
          'Livober': [50.45129000000003, 30.59734000000003], 'Darnytsia': [50.442360076605716, 30.62454998773769],
          'Cherniha': [50.45993000000004, 30.630400000000066], 'Lisova': [50.464090000000056, 30.644570000000044],
          'HeroiD': [50.52260000000007, 30.49794000000003], 'Minska': [50.51144000000005, 30.498060000000066],
          'Obolon': [50.50069000000008, 30.497510000000034], 'Pochaina': [50.48705000000007, 30.51818000000003],
          'Shevchenka': [50.473880000000065, 30.504180000000076],
          'Kontraktova': [50.463482693013326, 30.518751913902165], 'Poshtova': [50.4588977, 30.5224781],
          'Maidan ': [50.45132408684042, 30.522695826319136], 'Tolstoho': [50.43945000000008, 30.516990000000078],
          'Olimpiiska': [50.431940000000054, 30.51628000000005], 'PUkrayina': [50.420540000000074, 30.520880000000034],
          'Lybidska': [50.41298000000006, 30.52508000000006], 'Demiivska': [50.40477000000004, 30.51759000000004],
          'Holoseyka': [50.40477000000004, 30.51759000000004], 'Vasylkivska': [50.39354999148958, 30.4898899848531],
          'Vystavka': [50.381590000000074, 30.477500000000077], 'Ipodrom': [50.37704000000008, 30.47004000000004],
          'Teremky': [50.36751000000004, 30.45512000000008], 'Syrets': [50.47628000000003, 30.43001000000004],
          'Dorohozhychi': [50.47324000000003, 30.44876000000005], 'Lukianivska': [50.46245000000005, 30.48115000000007],
          'Zoloti': [50.447940000000074, 30.514140000000054], 'PSportu': [50.43825000000004, 30.520880000000034],
          'Klovska': [50.43709000000007, 30.531430000000057], 'Pecherska': [50.43228389377043, 30.54203508426261],
          'Druzhby': [50.417850000000044, 30.544030000000078], 'Vydubychi': [50.40291000000008, 30.55964000000006],
          'Slavutych': [50.43330003000731, 30.59418991949926], 'Osokorky': [50.39554000000004, 30.616520000000037],
          'Pozniaky': [50.39808000000005, 30.63373000000007], 'Kharkivska': [50.40342003332558, 30.681900001874112],
          'Vyrlytsia': [50.403770000000065, 30.66644000000008], 'Boryspilska': [50.404360000000054, 30.685410000000047],
          'CheKhutir': [50.409050000000036, 30.695370000000025]}


def dist(p, m):
    slat = radians(p[0])
    slon = radians(p[1])
    elat = radians(m[0])
    elon = radians(m[1])
    return 6371.01 * acos(sin(slat) * sin(elat) + cos(slat) * cos(elat) * cos(slon - elon))


def closest_stations(address='вул. Велика Житомирська, 20'):
    g = geocoder.arcgis('Kyiv,' + address).latlng
    distances = [{'station': metro, 'distance': dist(g, coords[metro])} for metro in coords]
    distances = sorted(distances, key=lambda el: el['distance'])
    rez = distances[0]['station'] + ' ' + distances[1]['station'] + ' ' + distances[2]['station']
    return rez


if __name__ == "__main__":
    print(closest_stations("вул. Велика Васильківськаб 52"))

    # neo = {}
    # for el in coords:
    #     i = stations.index(el)
    #     neo[shorts[i]]=coords[el]
