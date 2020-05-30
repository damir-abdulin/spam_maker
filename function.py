# Содержит функции для spam_maker
#
# GitHub: https://github.com/damir-abdulin/spam_maker.git 
# 29/05/2020

import vk_api

def registration():
    '''Если пароль не заполнен, то запрашивает вести логин и пароль.'''
    is_enter = input("Использовать сохраненные данные?(+/-) ")
    if is_enter == "+":
        try:
            with open('memory.txt','r') as memory_file:
                memory = eval(memory_file.read())
                login = memory['login']
                password = memory['password']
                return login, password
        except:
            print("Нет сохраненных данных для входа.\nВведите новые данные.")
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    is_save = input("Сохранить логин и пароль? (+/-) ")
        
    if is_save == "+":
        with open('memory.txt', 'w') as memory_file:
            data = {'login': login, 'password': password}
            memory_file.write(str(data))
            
    return login, password

def start_work(login, password):
    '''Начинает работу.'''
    while True:
        try:
            session = vk_api.VkApi(login, password)
            break
        except:
            print("В доступе отказанно.")
    
    # Настройка аккаунта
    session.auth()
    vk = session.get_api()
    
    return session, vk
    
def get_group(vk):
    '''Возвращает список групп.'''
    groups_full = vk.groups.get(user_id='592642016')
    groups = groups_full['items']

    return groups
