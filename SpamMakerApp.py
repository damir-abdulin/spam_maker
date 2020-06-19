import sys
import os
import vk_api

from PyQt5 import QtWidgets

import design
import function as func

class SpamMakerApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    ''' Класс GUI приложения, который наследуется от класса
        в файле design.
    '''
    def __init__(self, login, password, text, photo=None):
        super().__init__()
        self.setupUi(self) # Инициализация дизайна.
        
        self.login = login
        self.password = password
        self.text = text
        self.photo = photo
        
        self.btn_send_post.clicked.connect(self.start)
        
    def start(self):
        ''' Запусккает процесс отправки сообщений по группам. '''
        vk = self.start_work()
        groups = self.get_groups(vk)
        self.send_post(self.text, self.photo, vk, groups)
        
    def start_work(self):
        '''
            Открывает доступ к аккаунту.
            Запрашивает данные для входа и если эти данные верны,
            то возвращает рабочую сессию ВК.
        '''
        session = vk_api.VkApi(self.login, self.password)
        session.auth()
        vk = session.get_api()
                 
        return vk
    
    def get_groups(self, vk):
        '''
            Возвращает все группы пользователя в виде списка.
            
            Аргументы:
            vk -- информация для работы с vk_api. Получается с помощью функции
                start_work
        '''
        user_id = vk.users.get()[0]["id"]
        groups_full = vk.groups.get(user_id=vk.users.get()[0]["id"])
        
        # Получаем id всех групп.
        groups = groups_full['items']
        
        # Тестовые площадки.
        groups = [195666952, 195660207]
        
        return groups
        
    def send_post(self, text, photo, vk, groups):
        '''
            Отправляет записи во все группы из groups и выводит информацию
            о выполненной работе.
            
            Аргументы:
            vk -- информация для работы с vk_api. Получается с помощью функции
                start_work
            groups -- спиоск групп, в которые нудно отправить запись.
            text (str) -- текст записи. 
            photo (str) -- фотография, которую нужно прикрепить к записи.
                Требует свой id в виде 'photo598071478_457239148'
        '''
        for group in groups:
            try:
                post = vk.wall.post(owner_id=int(-(group)),
                    message=text, attachments=photo)
                self.print_result(vk, post, group, True)
            except:
                self.print_result(vk, post, group, False)

    def print_result(self, vk, post, group, flag):
        '''
            Выводит отредактированную на экран информацию о группе,
            в которую выложили пост, и о номера поста в данной группе в 
            удобном для чтении виде.
            
            Аргументы:
                post -- инофрмация об отпраленной записи.
                group -- группа, в которую отправлен пост.
                flag -- информация об успешности отправления записи.
                    True -- успех, а False -- ошибка.
        '''
        if flag:
            self.listWidget.addItem("Успешно отправлено")
            self.listWidget.addItem("Группа: " +
                vk.groups.getById(group_id = group)[0]["name"] + "")
            self.listWidget.addItem("Запись: " + str(post["post_id"]))
            self.listWidget.addItem("----------------")
        else:
            self.listWidget.addItem("Упс, что-то пошло не так.")
            self.listWidget.addItem("Группа: " +
                vk.groups.getById(group_id = group)[0]["name"] + "")
            self.listWidget.addItem("----------------")
