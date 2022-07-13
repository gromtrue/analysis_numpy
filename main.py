'''https://habr.com/ru/company/otus/blog/331746/'''
# Import pandas
import pandas as pd
# import numpy as np

# # Присваиваем имени файла электронной таблицы значение "file`
# file = r'C:\Users\gribanov_r\Desktop\2022.06.21 17.43 deliveries_today.xls'
#
# # Загружаем электронную таблицу
# xl = pd.ExcelFile(file)  # Для загрузки .csv используется аналогичная функция pd.read_csv
#
# # # Печатаем названия листов
# # print(xl.sheet_names)
#
# # Загружаем лист в фрейм данных по имени: df1
# df1 = xl.parse('TDSheet')
# # print(df1)
#
# '''Удаляем столбцы'''
# '''вызываем функцию drop() для нашего объекта, передавая параметр inplace как True и параметр оси как 1, что говорит
# Pandas об изменениях непосредственно в нашем объекте и что он должен искать значения, которые будут отброшены
# в столбцах объекта.'''
# to_drop = ['Unnamed: 1', 'Unnamed: 2', 'Unnamed: 5']  # Перечисляем стобцы для удаления
# df1.drop(to_drop, inplace=True, axis=1)
#
# # print(df1.head)
#
# df1 = df1.delete(df1, 0, 0)
# print(df1.head)


# importing numpy module
import numpy as np

# create an array with integers
# with 3 rows and 3 columns
a = np.array([[67, 65, 45],
              [45, 67, 43],
              [3, 4, 5],
              [52, 78, 65]])
# print("Original\n", a)

# # delete 1 st row
# data = np.delete(a, 0, 0)
# print("data after 1 st row deleted :\n", data)

# delete 1 st column
data = np.delete(a, [1, 2, 3], 0)
print("data after 1 st column deleted :\n", data)
