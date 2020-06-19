# Программа для автоматического отправления записей в группы ВК.
# Программа получает список групп и запись, которую необходимо отправить.
#
# GitHub: https://github.com/damir-abdulin/spam_maker.git 
import sys
import os
from PyQt5 import QtWidgets

from SpamMakerApp import SpamMakerApp

def main():
    text = (
        'Группа компаний "Серволюкс" объявляет конкурс на вакансию РАБОЧИХ БЕЗ ОПЫТА РАБОТЫ' +
        '\n\nРабочее место - ЗАО "Серволюкс Агро", аг. Межисетки,'+
        '\n\nЖдем Ваше резюме!'+
        '\n\nТелефон для справок: +375 (29) 747 35 32 Абдулина Ирина'+
        '\n\nРезюме просьба направлять на адрес: irina.abdulina@servolux.by'+
        '\n\n#Servolux #Серволюкс #работа #Могилев #Межисетки #Карьера #servoluxcareer'
    )
    photo = 'photo592642016_457239148'
    login = '+375297473532'
    password = 'Servolux2' 
    
    app = QtWidgets.QApplication(sys.argv)
    window = SpamMakerApp(login, password, text, photo)
    window.show()
    app.exec_()
    
if __name__ == '__main__':
    main()
