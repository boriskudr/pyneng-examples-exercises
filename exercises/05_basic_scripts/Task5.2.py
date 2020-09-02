#ip_net_prefix = input('Введите сеть и маску x.x.x.x/y: ')
ip_net_prefix = "10.1.1.0/2"

ip_net_prefix = ip_net_prefix.replace("/", ".").split(".")

mask_bits = "1"*int(ip_net_prefix[-1]) + "0"*(32 - int(ip_net_prefix[-1]))

mask = []

mask.append(mask_bits[:8])
mask.append(mask_bits[8:16])
mask.append(mask_bits[16:24])
mask.append(mask_bits[24:])

print("Network:")

print(f'{ip_net_prefix[0]:8} {ip_net_prefix[1]:8} {ip_net_prefix[2]:8} {ip_net_prefix[3]:8}')
print(f'{bin(int(ip_net_prefix[0])).replace("0b", ""):0>8} {bin(int(ip_net_prefix[1])).replace("0b", ""):0>8} {bin(int(ip_net_prefix[2])).replace("0b", ""):0>8} {bin(int(ip_net_prefix[3])).replace("0b", ""):0>8}')

print(f"\nMask:")
print(f"/{ip_net_prefix[-1]}")

print(f'{int(mask[0], 2):<8} {int(mask[1], 2):<8} {int(mask[2], 2):<8} {int(mask[3], 2):<8}')
print(f'{mask[0]:<8} {mask[1]:<8} {mask[2]:<8} {mask[3]:<8}')

