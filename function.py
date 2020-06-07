# Содержит функции для spam_maker
#
# GitHub: https://github.com/damir-abdulin/spam_maker.git 
# 29/05/2020
import vk_api

def start(text='test', photo=None):
    """
        Отправляет пост в группы, на которые подписан пользователь.
        Получает данные про запись, а возвращает
        информацию о том, где Ззапись размещена и номер этого поста.
        
        Аргументы:
        text (str) -- текст записи. 
        photo (str) -- фотография, которую нужно прикрепить к записи.
            Требует свой id в виде 'photo598071478_457239148'
    """
    vk = start_work()
    groups = get_groups(vk)
    send_post(vk, groups, text, photo)
    
def start_work():
    """
        Открывает доступ к аккаунту.
        Запрашивает данные для входа и если эти данные верны,
        то возвращает рабочую сессию ВК.
    """
    while True:
        try:
            login = input("Введите логин: ")
            password = input("Введите пароль: ")
            # Регистрация пользователя.
            session = vk_api.VkApi(login, password)
            session.auth()
            break
        except:
            print("Неверный пароль или логин. Повторите попытку")
    vk = session.get_api()
             
    return vk
    
def get_groups(vk):
    """
        Возвращает все группы пользователя в виде списка.
        
        Аргументы:
        vk -- информация для работы с vk_api. Получается с помощью функции
            start_work
    """
    user_id = vk.users.get()[0]["id"]
    groups_full = vk.groups.get(user_id=vk.users.get()[0]["id"])
    
    # Получаем id всех групп.
    groups = groups_full['items']
   
    return groups
    
def send_post(vk, groups, text, photo):
    """
        Отправляет записи во все группы из groups и выводит информацию
        о выполненной работе.
        
        Аргументы:
        vk -- информация для работы с vk_api. Получается с помощью функции
            start_work
        groups -- спиоск групп, в которые нудно отправить запись.
        text (str) -- текст записи. 
        photo (str) -- фотография, которую нужно прикрепить к записи.
            Требует свой id в виде 'photo598071478_457239148'
    """
    for group in groups:
        try:
            post = vk.wall.post(owner_id=int(-(group)),
                message=text, attachments=photo)
            print_result(vk, post, group, True)
        except:
            print_result(vk, post, group, False)

def print_result(vk, post, group, flag):
    """
        Выводит отредактированную на экран информацию о группе,
        в которую выложили пост, и о номера поста в данной группе в 
        удобном для чтении виде.
        
        Аргументы:
            post -- инофрмация об отпраленной записи.
            group -- группа, в которую отправлен пост.
            flag -- информация об успешности отправления записи.
                True -- успех, а False -- ошибка.
    """
    import colorama
    from colorama import Fore, Style
    
    colorama.init()

    if flag:
        print(Fore.GREEN + "Успешно отправлено")
        print(Style.RESET_ALL + "Группа: " +
            vk.groups.getById(group_id = group)[0]["name"] + "")
        print("Запись: " + str(post["post_id"]))
        print("----------------")
    else:
        print(Fore.RED + "Упс, что-то пошло не так.")
        print(Style.RESET_ALL + "Группа: " +
            vk.groups.getById(group_id = group)[0]["name"] + "")
        print("----------------")
