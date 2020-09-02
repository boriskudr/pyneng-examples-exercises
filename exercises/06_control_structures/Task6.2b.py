ipaddr_valid = False

while not ipaddr_valid:
    ipaddr = input("Введите IP адрес: ")
    ipaddr = ipaddr.split(".")
    if len(ipaddr) == 4 and 0 <= int(ipaddr[0]) <= 255 and 0 <= int(ipaddr[1]) <= 255 and 0 <= int(ipaddr[2]) <= 255 and 0 <= int(ipaddr[3]) <= 255:
        ipaddr_valid = "True"
        if 0 < int(ipaddr[0]) < 223:
            iptype = "unicast"
        elif 223 < int(ipaddr[0]) < 240:
            iptype = "multicast"
        elif ipaddr[0] == "255" and ipaddr[1] == "255" and ipaddr[2] == "255" and ipaddr[3] == "255":
            iptype = "local broadcast"
        elif ipaddr[0] == "0" and ipaddr[1] == "0" and ipaddr[2] == "0" and ipaddr[3] == "0":
            iptype = "unassigned"
        else:
            iptype = "unused"
        print(iptype)
    else:
        print("Неправильный IP-адрес")

print("Finished")
"""Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова."""

