from operator import itemgetter
"""CD-диск"""
class CD:
    def __init__(self, id, name_cd, cap, lib_id):
        self.id = id
        self.name_cd = name_cd # имя
        self.cap = cap # вместимость диска (Мегабайт) 
        self.lib_id = lib_id # в какой библиотеке
"""Библиотека CD-дисков"""
class lib:
    def __init__(self, id, name):
        self.id = id 
        self.name = name
class CdLib: 
    """связь многие ко многим"""
    def __init__(self, lib_id, cd_id):
        self.lib_id = lib_id 
        self.cd_id = cd_id
# библиотеки 
libs = [
    lib(1, 'Первая Библиотека'),
    lib(2, 'Вторая Библиотека'), lib(3, 'Третья Библиотека'),
    lib(4, 'Четвертая Библиотека'), lib(5, 'Пятая Библиотека'), lib(6, 'Шестая Библиотека'),
]
# CD-диски
cds = [
    CD(2, 'kodack', 2048, 1), CD(3, 'Samsung', 1024, 3), CD(4, 'Sharp', 3072, 4),
    CD(5, 'Sony', 4096, 5), CD(6, 'Piratsky', 2048, 1), CD(7, 'Palm', 512, 6), CD(8, 'IBM', 4096, 4), CD(9, 'Toshiba', 4096, 5)
]
cds_libs = [ CdLib(1,1), CdLib(1,2), CdLib(1,4), CdLib(1,8), CdLib(2,4), CdLib(2,5), CdLib(2,6), CdLib(2,1), CdLib(3,3), CdLib(4,1), CdLib(4,5), CdLib(5,4), CdLib(5,2), CdLib(6,7),
]
def main():
    """Основная функция"""
    # Соединение данных один-ко-многим 
    one_to_many = [(h.name_cd, h.cap, p.name)
        for p in libs
        for h in cds
        if h.lib_id==p.id]
    # Соединение данных многие-ко-многим 
    many_to_many_temp = [(p.name, ph.lib_id, ph.cd_id)
        for p in libs
        for ph in cds_libs if p.id==ph.lib_id]
    many_to_many = [(h.name_cd, h.cap, lib_name)
        for lib_name, lib_id, cd_id in many_to_many_temp for h in cds if h.id==cd_id]
    print('Задание E1')
    res_E1 = []
    for name_cd, cap, name in one_to_many:
        if 'Первая' in name: # Ищем бибилиотеки с ключевым словом "Вторая"
            res_E1.append((name, name_cd)) 
    print(res_E1)
    print('\nЗадание E2') # находим среднюю вместимость дисков 
    res_E2_unsorted = [] # Перебираем все бибилиотеки
    for p in libs:# Список дисков библиотеки
        list_cd = list(filter(lambda i: i[2]==p.name, one_to_many)) # Если в библиотеке есть диск
    if len(list_cd) > 0:# вместимомть CD
        list_cap = [cap for _,cap,_ in list_cd]
    # средняя вместимость
    avg_sum = sum(list_cap)/len(list_cap) 
    res_E2_unsorted.append((p.name, avg_sum))
    res_E2 = sorted(res_E2_unsorted, key=itemgetter(1))
    print('Средний объем дисков: ')
    print(avg_sum) 
    print(res_E2)
    print('\nЗадание E3')
    # находим диски, начинающиеся с "P" и выводим их библиотеки 
    res_E3 = []
    for name_cd, cap, name in many_to_many:
        if name_cd.find("P") == 0: 
            res_E3.append((name_cd, name))
    print(res_E3)
if __name__ == '__main__': 
    main()