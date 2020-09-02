#ipaddr = "10.1.2.3"
#ipaddr = "224.1.2.3"
#ipaddr = "255.255.255.255"
#ipaddr = "0.0.0.0"
ipaddr = "240.1.1.1"

ipaddr = ipaddr.split(".")

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
'''Запросить у пользователя ввод IP-адреса в формате 10.0.1.1

Определить тип IP-адреса.

В зависимости от типа адреса, вывести на стандартный поток вывода:
„unicast“ - если первый байт в диапазоне 1-223
„multicast“ - если первый байт в диапазоне 224-239
„local broadcast“ - если IP-адрес равен 255.255.255.255
„unassigned“ - если IP-адрес равен 0.0.0.0
„unused“ - во всех остальных случаях
'''