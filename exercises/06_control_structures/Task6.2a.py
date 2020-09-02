#ipaddr = "10.1.2.3"
#ipaddr = "224.1.2.3"
#ipaddr = "255.255.255.255"
#ipaddr = "0.0.0.0"
ipaddr = "10.0.1.1"

ipaddr = ipaddr.split(".")

if len(ipaddr) == 4 and 0 <= int(ipaddr[0]) <= 255 and 0 <= int(ipaddr[1]) <= 255 and 0 <= int(ipaddr[2]) <= 255 and 0 <= int(ipaddr[3]) <= 255:
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


'''Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:

состоит из 4 чисел разделенных точкой,
каждое число в диапазоне от 0 до 255.
Если адрес задан неправильно, выводить сообщение: „Неправильный IP-адрес'''
