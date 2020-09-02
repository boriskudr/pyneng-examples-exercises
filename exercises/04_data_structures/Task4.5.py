command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

c1_set = command1.split()[-1]
c2_set = command2.split()[-1]

c1_set = set(c1_set.split(","))
c2_set = set(c2_set.split(","))

print(sorted(c1_set & c2_set))
