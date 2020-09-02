access_template = [
    'switchport mode access', 'switchport access vlan',
    'spanning-tree portfast', 'spanning-tree bpduguard enable'
]

trunk_template = [
    'switchport trunk encapsulation dot1q', 'switchport mode trunk',
    'switchport trunk allowed vlan'
]

access = {
    '0/12': '10',
    '0/14': '11',
    '0/16': '17',
    '0/17': '150'
}

trunk = {
        '0/1': ['add', '10', '20'],
        '0/2': ['only', '11', '30'],
        '0/4': ['del', '17']
    }

for intf, vlan in access.items():
    print('interface FastEthernet' + intf)
    for command in access_template:
        if command.endswith('access vlan'):
            print(' {} {}'.format(command, vlan))
        else:
            print(' {}'.format(command))

for intf, vlan in trunk.items():
    print('interface FastEthernet' + intf)
    for command in trunk_template:
        if command.endswith('allowed vlan'):
            if vlan[0] == 'add':
                print(' {} {} {}'.format(command, 'add', ",".join(vlan[1:])))
            elif vlan[0] == 'only':
                print(' {} {}'.format(command, ",".join(vlan[1:])))
            elif vlan[0] == 'del':
                print(' {} {} {}'.format(command, 'remove', ",".join(vlan[1:])))
            else:
                print("Неправильный ввод")
        else:
            print(' {}'.format(command))

'''в соответствии каждому порту стоит список и первый (нулевой) элемент списка указывает как воспринимать номера VLAN, которые идут дальше:

add - VLANы надо будет добавить (команда switchport trunk allowed vlan add 10,20)
del - VLANы надо удалить из списка разрешенных (команда switchport trunk allowed vlan remove 17)
only - на интерфейсе должны остаться разрешенными только указанные VLANы (команда switchport trunk allowed vlan 11,30)
Задача для портов 0/1, 0/2, 0/4:

сгенерировать конфигурацию на основе шаблона trunk_template
с учетом ключевых слов add, del, only'''