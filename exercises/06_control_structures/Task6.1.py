mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']
mac_cisco = []
for i in range(len(mac)):
    mac_cisco.append(mac[i].replace(":", "."))

print(mac_cisco)