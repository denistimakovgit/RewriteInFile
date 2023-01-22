import glob, os
import inspect

"""
создаем словарь как основной объект для работы в дальнейшем
ключом словаря будет размер текстового файла
значением будет список из пути к файлу и количества строк
Пример словаря:
49: ['/Users/denistimakov/PycharmProjects/RewriteInFile/2.txt', '1'],
"""
files = {}

file_path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
name = os.path.basename('/Users/denistimakov/PycharmProjects/RewriteInFile/1.txt')

for file in glob.glob("*.txt"): # для каждого текстового файла возвращаем список имен путей
    full_path = file_path + '/' + file #создаем ссылку на файл из его пути и самого файла с расширением
    file_size = os.path.getsize(full_path) # определяем размер файла
    with open(full_path, 'rt', encoding='utf-8') as file_to_count:
        rows_count = str(len(file_to_count.readlines())) # определяем кол-во строк в файле
    files[file_size] = [full_path, rows_count] # записываем в словарь полученный результат

sorted_files = dict(sorted(files.items(), key=lambda x: x[0])) # сортируем по возрастанию ключа словарь

for key, value in sorted_files.items():
    with open(value[0], 'rt', encoding='utf-8') as input_file:
        with open("3.txt", 'a') as output_file:
            output_file.writelines(os.path.basename(value[0]))
            output_file.writelines('\n')
            output_file.writelines(value[1])
            output_file.writelines('\n')
            for line in input_file:
                output_file.write(line)
            output_file.writelines('\n')
            output_file.writelines('\n')
        output_file.close()
    input_file.close()

