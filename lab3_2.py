import twitter2
import json


def create_file(id_var):
    twitter2.create_json_file(id_var)

def open_and_read_json_file(file):
    f = open(file,encoding = 'utf-8')
    ff = json.load(f)
    return ff


def main():
    id_var = input('Type your twitter id: ')
    create_file(id_var)
    f = open_and_read_json_file('info.json')
    lst = []
    ff = f
    ex = 0
    while True:
        print('Elements: ',end = '')
        space_ind = 0
        for el in ff:
            if space_ind == 1:
                print(', ' + str(el),end = '')
            else:
                print(str(el),end = '')
            space_ind = 1
        if ex == 0:
            choise = input('\nType: ')
        else:
            choise = int(input('\nType number from 1 to ' + str(len(ff)) + ': '))
            ex = 0
        lst.append(choise)
        try:
            if not type(choise) == int:
                if type(ff[choise]) == dict:
                    ff = ff[choise]
                elif type(ff[choise]) == list:
                    ff = ff[choise]
                    ex = 1
                else:
                    print('Answer: ' + str(ff[choise]))
                    print('History of selections: ' + str(lst))
                    break
            else:
                ff = ff[choise-1]
        except:
            print('Wrong atribute')
main()
