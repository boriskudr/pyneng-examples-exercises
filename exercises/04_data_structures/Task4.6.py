ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

out_fields = '''Protocol:,Prefix:,AD/Metric:,Next-Hop:,Last update:,OutboundInterface:'''

out_fields = out_fields.split(',')

ospf_route = ospf_route.replace("O","OSPF")
ospf_route = ospf_route.replace("[","")
ospf_route = ospf_route.replace("]","")
ospf_route = ospf_route.replace(",", "").split()
ospf_route.remove('via')


for i in range(len(ospf_route)):
    print(f'{out_fields[i]:18} {ospf_route[i]}')
