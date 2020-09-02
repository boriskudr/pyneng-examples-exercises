import sys

ignore = ['duplex', 'alias', 'Current configuration']

file_name = sys.argv[1]

with open(file_name, "r") as f, open("config_sw1_cleared.txt", "w") as cleared_f:
    for line in f:
        for word in ignore:
            if word in line:
                break
        else:
            cleared_f.write("{}".format("".join(line)))

'''Дополнить скрипт из задания 7.2a: вместо вывода на стандартный поток вывода, скрипт должен записать полученные строки в файл config_sw1_cleared.txt

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore. Строки, которые начинаются на ! отфильтровывать не нужно.'''
