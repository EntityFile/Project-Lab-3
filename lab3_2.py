import twitter2
import json


def open_and_read_json_file(file):
    f = open(file,encoding = 'utf-8')
    ff = json.load(f)
    return ff

def main():
    ff = open_and_read_json_file('info.json')
    for el in ff['users']:
        print(el)
main()