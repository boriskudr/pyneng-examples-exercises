mac = 'AAAA:BBBB:CCCC'

mac = mac.replace(":",'')

mac = bin(int(mac, 16))
mac = mac[2:]

print(f'{mac}')