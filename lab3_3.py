import folium
import geopy
import json


def open_and_read_json_file(file):
    f = open(file,encoding = 'utf-8')
    ff = json.load(f)
    return ff

def create_friends_layer(map, ff):
    fg_friends = folium.FeatureGroup(name="Films")
    names_dict = dict()
    for inf in ff['users']:
        try:
            names_dict[inf['location']].append(inf['screen_name'])
        except:
            names_dict[inf['location']] = [inf['screen_name']]
    print(names_dict)
    for el in names_dict:
        create_geocoder = geopy.geocoders.Bing('Av7RE8z6Aw7I7yPq_0\
        yUv26n7uCxcfwVz1gfl0RvHWmEoYk0U8l_3FFf0mEKmgoA')
        try:
            create_cords = create_geocoder.geocode(el)
            fg_friends.add_child(folium.Marker(location=[create_cords.latitude,\
                             create_cords.longitude], popup=' | '.join(names_dict[el]),\
                              icon=folium.Icon(color='darkblue', icon='info-sign')))
            print('add',el)
        except:
            print(el)
    map.add_child(fg_friends)
    map.add_child(folium.LayerControl())
    return map

def main():
    ff = open_and_read_json_file('info.json')
    map = folium.Map()
    map = create_friends_layer(map, ff)
    map.save('templates/map.html')