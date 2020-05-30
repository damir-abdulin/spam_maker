# Программа для автоматического отправления записей в группы ВК.
# Программа получает список групп и запись, которую необходимо отправить.
#
# GitHub: https://github.com/damir-abdulin/spam_maker.git 
# 23/05/2020

import vk_api

import function as f

login, password = f.registration()
session, vk = f.start_work(login, password)

# Оформление записи.
message = (
    'Группа компаний "Серволюкс" объявляет конкурс на вакансию РАБОЧИХ БЕЗ ОПЫТА РАБОТЫ' +
    '\n\nРабочее место - ЗАО "Серволюкс Агро", аг. Межисетки,'+
    '\n\nЖдем Ваше резюме!'+
    '\n\nТелефон для справок: +375 (29) 747 35 32 Абдулина Ирина'+
    '\n\nРезюме просьба направлять на адрес: irina.abdulina@servolux.by'+
    '\n\n#Servolux #Серволюкс #работа #Могилев #Межисетки #Карьера #servoluxcareer'
    )
photo = 'photo598071478_457239148'

groups = f.get_group(vk)
for group in groups:
    try:
        post = vk.wall.post(owner_id=int(-(group)), message=message, attachments=photo)
        print("Успешно отправлено")
        print("Группа: " + vk.groups.getById(group_id = group)[0]["name"] + "")
        print("Пост: " + str(post["post_id"]))
        print("----------------")
    except:
        print("Упс, что-то пошло не так.")
        print("Группа: " + vk.groups.getById(group_id = group)[0]["name"] + "")
        print("----------------")
