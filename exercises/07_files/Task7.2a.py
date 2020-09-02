import sys

ignore = ['duplex', 'alias', 'Current configuration']

file_name = sys.argv[1]

with open(file_name, "r") as f:
    for line in f:
        if not line.startswith("!"):
            for word in ignore:
                if word in line:
                    break
            else:
                print("{}".format("".join(line.rstrip().split('\n'))))


'''Дополнить скрипт: Скрипт не должен выводить команды, в которых содержатся слова, которые указаны в списке ignore'''