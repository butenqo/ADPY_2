import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as file:
    rows = csv.reader(file)
    contacts_list = list(rows)

for j in contacts_list:
    fio = ' '.join(j[:2]).rstrip().split(' ')
    j[0:len(fio)] = fio

dict = {}

for t in contacts_list:
    if (f'{t[1]} {t[0]}') in dict:

        if dict[f'{t[1]} {t[0]}'][0] == '':
            dict[f'{t[1]} {t[0]}'][0] = t[2]

        if dict[f'{t[1]} {t[0]}'][1] == '':
            dict[f'{t[1]} {t[0]}'][1] = t[3]

        if dict[f'{t[1]} {t[0]}'][2] == '':
            dict[f'{t[1]} {t[0]}'][2] = t[4]

        if dict[f'{t[1]} {t[0]}'][3] == '':
            dict[f'{t[1]} {t[0]}'][3] = t[5]

        if dict[f'{t[1]} {t[0]}'][4] == '':
            dict[f'{t[1]} {t[0]}'][4] = t[6]
    else:
        dict[f'{t[1]} {t[0]}'] = [t[2], t[3], t[4], t[5], t[6]]
        


list=[]
for i in dict:
    list.append((i.split(' ')) + dict[i])

pattern = r'(\+7|8|7)[\s]?\(*(\d{3})\)*[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})[\s\.\(]?[\s\.\(]?(доб. )?(\d{4})?(\))?'
subs = r'+7(\2)\3-\4-\5 \6\7'


for i in list:
    i[5]= re.sub(pattern, subs, i[5])

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(list)